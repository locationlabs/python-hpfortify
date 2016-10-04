from click import (
    Choice,
    command,
    option,
    Path,
)
from sys import exit

from hpfortify.api.application import ApplicationApi
from hpfortify.api.auth import AuthApi
from hpfortify.api.release import ReleaseApi
from hpfortify.api.static_scans import StaticScanApi
from hpfortify.model.application import (
    SdlcStatusType,
)
from hpfortify.model.common import (
    ASSESSMENT_TYPE_ID,
)
from hpfortify.model.release import (
    PostReleaseRequest,
    PostReleaseResponse,
)
from hpfortify.model.scan import (
    TechnologyStack,
    EntitlementFrequencyType,
)
from hpfortify.model.scan import (
    PostStartScanResponse,
)
from hpfortify.model.utils import (
    print_response
)


class EnumParameterType(Choice):
    """The enum type allows a value to be checked against the values in an
    enumeration type. The command receives an instance of the Enum type.
    """
    def __init__(self, enum_class):
        super(EnumParameterType, self).__init__([enum.name for enum in enum_class])  # noqa
        self.enum_class = enum_class

    def convert(self, value, param, ctx):
        name = super(EnumParameterType, self).convert(value, param, ctx)
        return self.enum_class[name]


@command()
@option(
    "--api-key",
    type=str,
    required=True,
    help="HPfotify api key required to make api calls"
)
@option(
    "--api-secret",
    type=str,
    required=True,
    help="HPfortify secret which is associated with api key. This is required to make api calls"  # noqa
)
@option(
    "--app-name",
    type=str,
    required=True,
    help="Application name"
)
@option(
    "--release-name",
    type=str,
    required=True,
    help="Release Name"
)
@option(
    "--previous-release-name",
    type=str,
    default=None,
    required=False,
    help="""Previous release name in case you want to copy the scan state
         from the previous release. This parameter is only valid when you
         the release is not already existing and it is going to create a
         new release.
         """
)
@option(
    "--file-path",
    type=Path(exists=True),
    required=True,
    help="Zipped source code file path"
)
@option(
    "--sdlc-status",
    type=EnumParameterType(SdlcStatusType),
    default=SdlcStatusType.PRODUCTION,
    help="SDLC status type. It could be one of these: Development, Production, QA, Retired"  # noqa
)
@option(
    "--technology-stack",
    type=EnumParameterType(TechnologyStack),
    default=TechnologyStack.ANDROID,
    help="Technology stack. example Android, PYTHON, Ruby etc.",
)
@option(
    "--entitlement-id",
    type=int,
    required=True,
    help="Entitlement id which should be used for this scan.",
)
@option(
    "--entitlement-frequency-type",
    type=EnumParameterType(EntitlementFrequencyType),
    default=EntitlementFrequencyType.SUBSCRIPTION,
    help="Entitlement frequency type example: Subscription or SingleScan",
)
def start_static_scan(api_key,
                      api_secret,
                      app_name,
                      release_name,
                      previous_release_name,
                      file_path,
                      sdlc_status,
                      technology_stack,
                      entitlement_id,
                      entitlement_frequency_type,
                      ):
    """
    This method starts the scan.
    """
    is_authorized = False
    try:
        auth_api = AuthApi(api_key=api_key.encode('utf8'), api_secret=api_secret.encode('utf8'))
        # Get the access token first
        auth_response = auth_api.authorize()
        is_authorized = True
        # Fetch the application
        application = fetch_app(auth_response.access_token,
                                app_name)

        print_response(application, "Application response")
        release_api = ReleaseApi(access_token=auth_response.access_token)
        # Get the current release
        release = create_or_fetch_release(release_api,
                                          application.application_id,
                                          release_name,
                                          previous_release_name,
                                          sdlc_status,
                                          )
        print_response(release, "Release response")
        # Look for scan if there is already scan existing then request for
        is_remediation_scan = release_api.is_static_scan_present(release.release_id)
        print "is remediation scan: {}".format(is_remediation_scan)
        # remediation scan (Remediation scan is free). Otherwise start a
        # regular static scan.
        static_scan_api = StaticScanApi(access_token=auth_response.access_token)
        scan_response = static_scan_api.post_static_scans(file_path,
                                                          release.release_id,
                                                          ASSESSMENT_TYPE_ID,
                                                          technology_stack.value,
                                                          entitlement_id,
                                                          entitlement_frequency_type.value,
                                                          is_remediation_scan=is_remediation_scan,
                                                          )
        if type(scan_response) is not PostStartScanResponse:
            print "Couldn't start scan"
            exit(-1)
        print_response(scan_response)
    finally:
        if is_authorized:
            auth_api.expire_access_token()

# ---------------- Utility methods --------------------


def create_or_fetch_release(release_api,
                            app_id,
                            release_name,
                            previous_release_name,
                            sdlc_status_type,
                            ):
    app_api = ApplicationApi(access_token=release_api.access_token)
    copy_state = False
    # find the current release
    current_release = app_api.get_release_by_application_and_release_name(app_id,
                                                                          release_name,
                                                                          )
    if current_release:
        return current_release
    else:
        # Current release is not there create new release.
        if previous_release_name:
            # User wants to copy
            copy_state = True
            previous_release = app_api.get_release_by_application_and_release_name(app_id,
                                                                                   release_name,
                                                                                   )
            if not previous_release:
                print "could not find the previous release: {}".format(
                    previous_release_name,
                )
                exit(-1)

        if not create_release(release_api,
                              app_id,
                              release_name,
                              copy_state,
                              previous_release.release_id,
                              sdlc_status_type,
                              ):
            print "couldn't create release"
            exit(-1)
        # Once release is created fetch the release and return.
        return app_api.get_release_by_application_and_release_name(app_id,
                                                                   release_name,
                                                                   )


def create_release(release_api,
                   app_id,
                   release_name,
                   copy_from_previous=False,
                   previous_release_id=None,
                   sdlc_status_type=SdlcStatusType.PRODUCTION.value,
                   ):
    post_release_request = PostReleaseRequest(application_id=app_id,
                                              release_name=release_name,
                                              release_description=None,
                                              copy_state=copy_from_previous,
                                              copy_state_release_id=previous_release_id if copy_from_previous else None,  # noqa
                                              sdlc_status_type=sdlc_status_type,
                                              )

    post_release_response = release_api.post_release(post_release_request)

    if type(post_release_response) is PostReleaseResponse:
        return True
    else:
        return False


def fetch_app(access_token, app_name):
    app_api = ApplicationApi(access_token=access_token)
    application = app_api.get_application_by_name(app_name)
    if not application:
        print "could not find application: {}\n Please check app name.".format(app_name)
        exit(-1)
    else:
        return application
