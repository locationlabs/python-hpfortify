from click import (
    Choice,
    command,
    option,
)

from hpfortify.model.application import (
    SdlcStatusType,
)


class EnumParameterType(Choice):
    """The enum type allows a value to be checked against the values in an
    enumeration type.  The command receives an instance of the Enum type.
    """
    def __init__(self, enum_class):
        super(EnumParameterType, self).__init__([enum.name for enum in enum_class])  # noqa
        self.enum_class = enum_class

    def convert(self, value, param, ctx):
        name = super(EnumParameterType, self).convert(value, param, ctx)
        return self.enum_class[name]


@command()
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
    "--file-path",
    type=str,
    required=True,
    help="Zipped source code file path"
)
@option(
    "--previous-release-name",
    type=str,
    default=None,
    required=False,
    help="Previous release name in case you want to copy the scan state from previous release"  # noqa
)
@option(
    "--sdlc-status",
    type=EnumParameterType(SdlcStatusType),
    default=SdlcStatusType.PRODUCTION,
    help="SDLC status type. It could be one of these: Development, Production, QA, Retired"  # noqa
)
def start_static_scan(app_name,
                      release_name,
                      file_path,
                      previous_release_name=None):
    """
    This method starts the scan.
    """
    # Get the access token first
    # Fetch the application

    # Check for existing release.

    # If there is not existing release then create one and copy
    # the state from previous release.

    # Look for scan if there is already scan existing then request for
    # remediation scan (Remediation scan is free). Otherwise start a
    # regular static scan.

    pass
