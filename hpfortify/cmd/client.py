from click import (
    Choice,
    command,
    option,
)
from json import dumps
from os import path
from sys import exit

from hpfortify.api.application import (
    get_application_by_name,
    get_release_by_application_and_release_name,
)
from hpfortify.api.auth import (
    authorize,
    expire_access_token,
)
from hpfortify.api.releae import (
    is_static_scan_present,
    post_release,
)
from hpfortify.api.static_scans import (
    post_static_scans,
)
from hpfortify.api.util import (
    BASE_URL_US,
)
from hpfortify.model.application import (
    SdlcStatusType,
)
from hpfortify.model.release import (
    PostReleaseRequest
)
from hpfortify.model.scan import (
    TechnologyStack,
    EntitlementFrequencyType,
)

# Constants
ASSESSMENT_TYPE_ID = 163  # Mobile static scan


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
    type=str,
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
    # Validate the data input parameters
    if not file_path or not path.isfile(file_path):
        print "File path is wrong: '{}'".format(file_path)
    is_authorized = False
    try:
        # Get the access token first
        auth_response = authorize(BASE_URL_US, api_key, api_secret)
        is_authorized = True

        # Fetch the application
        application = fetch_app(BASE_URL_US,
                                auth_response.access_token,
                                app_name)

        # Get the current release
        release = create_or_fetch_release(BASE_URL_US,
                                          auth_response.access_token,
                                          application.application_id,
                                          release_name,
                                          previous_release_name,
                                          sdlc_status,
                                          )

        # Look for scan if there is already scan existing then request for
        is_remediation_scan = is_static_scan_present(BASE_URL_US,  # noqa
                                                     auth_response.access_token,  # noqa
                                                     release.release_id)
        # remediation scan (Remediation scan is free). Otherwise start a
        # regular static scan.
        scan_response = post_static_scans(BASE_URL_US,
                                          auth_response.access_token,
                                          file_path,
                                          release.release_id,
                                          ASSESSMENT_TYPE_ID,
                                          technology_stack,
                                          entitlement_id,
                                          entitlement_frequency_type,
                                          is_remediation_scan,
                                          )

        print dumps(scan_response.to_dict(),
                    indent=3,
                    sort_keys=True,
                    )
    finally:
        if is_authorized:
            expire_access_token(BASE_URL_US, auth_response.access_token)

# ---------------- Utility methods --------------------


def create_or_fetch_release(base_url,
                            access_token,
                            app_id,
                            release_name,
                            previous_release_name,
                            sdlc_status_type,
                            ):
    copy_state = False
    # find the current release
    current_release = get_release_by_application_and_release_name(base_url,
                                                                  access_token,
                                                                  app_id,
                                                                  release_name,
                                                                  )
    if current_release:
        return current_release
    else:
        # Current release is not there create new release.
        if previous_release_name:
            # User wants to copy
            copy_state = True
            previous_release = get_release_by_application_and_release_name(base_url,  # noqa
                                                                           access_token,  # noqa
                                                                           app_id,  # noqa
                                                                           release_name,  # noqa
                                                                           )
            if not previous_release:
                print "could not find the previous release: {}".format(
                    previous_release_name,
                )
                exit(-1)

        create_release(base_url,
                       access_token,
                       app_id,
                       release_name,
                       copy_state,
                       previous_release.release_id,
                       sdlc_status_type,
                       )
        # Once release is created fetch the release and return.
        return get_release_by_application_and_release_name(base_url,
                                                           access_token,
                                                           app_id,
                                                           release_name,
                                                           )


def create_release(base_url,
                   access_token,
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
                                              sdlc_status_type=sdlc_status_type,  # noqa
                                              )

    post_release(base_url,
                 access_token,
                 post_release_request)


def fetch_app(base_url, access_token, app_name):

    application = get_application_by_name(base_url, access_token, app_name)
    if not application:
        print "could not find application: {}\n Please check app name.".format(app_name)  # noqa
        exit(-1)
    else:
        return application
