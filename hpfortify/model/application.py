from enum import Enum

from hpfortify.model.common import (
    SuccessAndErrorsResponse
)
from hpfortify.model.utils import (
    remove_none_value,
)


class Application(object):

    def __init__(self,
                 application_id,
                 application_name,
                 application_description,
                 application_created_date,
                 business_criticality_type_id,
                 business_criticality_type,
                 email_list,
                 application_type_id,
                 application_type,
                 attributes,
                 ):
        self.application_id = application_id
        self.application_name = application_name
        self.application_description = application_description
        self.application_created_date = application_created_date
        self.business_criticality_type_id = business_criticality_type_id
        self.business_criticality_type = business_criticality_type
        self.email_list = email_list
        self.application_type_id = application_type_id
        self.application_type = application_type
        self.attributes = attributes

    def to_dict(self):
        return dict(applicationId=self.application_id,
                    applicationName=self.application_name,
                    applicationDescription=self.application_description,
                    applicationCreatedDate=self.application_created_date,
                    businessCriticalityTypeId=self.business_criticality_type_id,  # noqa
                    businessCriticalityType=self.business_criticality_type,
                    emailList=self.email_list,
                    applicationTypeId=self.application_type_id,
                    applicationType=self.application_type,
                    attributes=[attribute.to_dict() for attribute in self.attributes]  # noqa
                        if self.attributes else None,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(
            application_id=dct.get("applicationId"),
            application_name=dct.get("applicationName"),
            application_description=dct.get("applicationDescription"),
            application_created_date=dct.get("applicationCreatedDate"),
            business_criticality_type_id=dct.get("businessCriticalityTypeId"),
            business_criticality_type=dct.get("businessCriticalityType"),
            email_list=dct.get("emailList"),
            application_type_id=dct.get("applicationTypeId"),
            application_type=dct.get("applicationType"),
            attributes=[ApplicationAttributeExtended.from_dict(
                    attribute,
                )
                for attribute in dct.get("attributes")] if dct.get("attributes") else None,  # noqa
            )


class ApplicationAttributeExtended(object):

    def __init__(self,
                 name=None,
                 id=None,
                 value=None,
                 ):
        """
        :param name: (optional) name of attribute
        :type name: string
        :param id:  (optional) id of attribute
        :type id: integer
        :param value: (optional) value of attribute
        :type value: string
        """
        self.name = name
        self.id = id
        self.value = value

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        return cls(name=dct.get("name"),
                   id=dct.get("id"),
                   value=dct.get("value"))


class ApplicationListResponse(object):

    def __init__(self,
                 items,
                 total_count,
                 ):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items],
                    totalCount=self.total_count)

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[Application.from_dict(item) for item in dct.get("items")],  # noqa
                   total_count=dct.get("total_count"),
                   )


class ApplicationType(Enum):
    """
    Enum class which represents Application type. It is used for making
    application request.
    """
    WEB_THICK_CLIENT = "Web_Thick_Client"
    MOBILE = "Mobile"


class ApplicationUser(object):

    def __init__(self,
                 user_id=None,
                 first_name=None,
                 last_name=None,
                 ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return dict(userId=self.user_id,
                    firstName=self.first_name,
                    lastName=self.last_name,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(user_id=dct.get("userId"),
                   first_name=dct.get("firstName"),
                   last_name=dct.get("lastName"),
                   )


class ApplicationUserListResponse(object):

    def __init__(self, items=None, total_count=None):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,  # noqa
                    totalCount=self.total_count,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[ApplicationUser.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                   total_count=dct.get("totalCount"),
                   )


class ApplicationUserPermissions(object):

    def __init__(self,
                 start_dynamic_scan=None,
                 start_mobile_scan=None,
                 start_static_scan=None,
                 create_release=None,
                 audit_issues=None,
                 challenge_issues=None,
                 edit_issues=None,
                 download_FPR=None,
                 ):
        self.start_dynamic_scan = start_dynamic_scan
        self.start_mobile_scan = start_mobile_scan
        self.start_static_scan = start_static_scan
        self.create_release = create_release
        self.audit_issues = audit_issues
        self.challenge_issues = challenge_issues
        self.edit_issues = edit_issues
        self.download_FPR = download_FPR

    def to_dict(self):
        return dict(startDynamicScan=self.start_dynamic_scan,
                    startMobileScan=self.start_mobile_scan,
                    startStaticScan=self.start_static_scan,
                    createRelease=self.create_release,
                    auditIssues=self.audit_issues,
                    challengeIssues=self.challenge_issues,
                    editIssues=self.edit_issues,
                    downloadFPR=self.download_FPR,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(start_dynamic_scan=dct.get("startDynamicScan"),
                   start_mobile_scan=dct.get("startMobileScan"),
                   start_static_scan=dct.get("startStaticScan"),
                   create_release=dct.get("createRelease"),
                   audit_issues=dct.get("auditIssues"),
                   download_FPR=dct.get("downloadFPR"),
                   )


class BusinessCriticalityType(Enum):
    """
    Enum class which represents the Business Criticality type. It is used for
    making application request.
    """
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class DeleteApplicationResponse(SuccessAndErrorsResponse):

    def __init__(self, success=None, errors=None):
        super(self.__class__, self).__init__(success=success, errors=errors)


class GetApplicationUsersResponse(object):

    def __init__(self, application_id=None, users=None):
        self.application_id = application_id
        self.users = users

    def to_dict(self):
        return dict(applicationId=self.application_id,
                    users=[item.to_dict() for item in self.users] if self.users else None,  # noqa
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(application_id=dct.get("applicationId"),
                   users=[ApplicationUser.from_dict(item) for item in dct.get("users")] if dct.get("users") else None,  # noqa
                   )


class GetAutoReportResponse(object):

    def __init__(self,
                 static_scan_report_id=None,
                 static_scan_report_name=None,
                 dynamic_scan_report_id=None,
                 dynamic_scan_report_name=None,
                 ):
        self.static_scan_report_id = static_scan_report_id
        self.static_scan_report_name = static_scan_report_name
        self.dynamic_scan_report_id = dynamic_scan_report_id
        self.dynamic_scan_report_name = dynamic_scan_report_name

    def to_dict(self):
        return dict(staticScanReportId=self.static_scan_report_id,
                    staticScanReportName=self.static_scan_report_name,
                    dynamicScanReportId=self.dynamic_scan_report_id,
                    dynamicScanReportName=self.dynamic_scan_report_name,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(static_scan_report_id=dct.get("staticScanReportId"),
                   static_scan_report_name=dct.get("staticScanReportName"),
                   dynamic_scan_report_id=dct.get("dynamicScanReportId"),
                   dynamic_scan_report_name=dct.get("dynamicScanReportName"),
                   )


class PostApplicationRequest(object):

    def __init__(self,
                 application_name=None,
                 application_description=None,
                 application_type=None,
                 release_name=None,  # This is mandatory field.
                 release_description=None,
                 email_list=None,
                 owner_id=None,
                 attributes=None,
                 business_criticality_type=None,
                 sdlc_status_type=None,
                 ):
        self.application_name = application_name
        self.application_description = application_description
        self.application_type = application_type
        self.release_name = release_name
        self.release_description = release_description
        self.email_list = email_list
        self.owner_id = owner_id
        self.attributes = attributes
        self.business_criticality_type = business_criticality_type
        self.sdlc_status_type = sdlc_status_type

    def to_dict(self):
        dct = dict(applicationName=self.application_name,
                   applicationDescription=self.application_description,
                   applicationType=self.application_type.value,
                   releaseName=self.release_name,
                   releaseDescription=self.release_description,
                   emailList=self.email_list,
                   ownerId=self.owner_id,
                   attributes=[item.to_dict() for item in self.attributes] if self.attributes else None,  # noqa
                   businessCriticalityType=self.business_criticality_type.value,  # noqa
                   sdlcStatusType=self.sdlc_status_type.value,
                   )
        # HPfortify doesn't like the key whose value is None. so remove those
        # entries before sending it to the server.
        return remove_none_value(dct)

    @classmethod
    def from_dict(cls, dct):
        return cls(application_name=dct.get("applicationName"),
                   application_description=dct.get("applicationDescription"),
                   application_type=ApplicationType(dct.get("applicationType")),  # noqa
                   release_name=dct.get("releaseName"),
                   release_description=dct.get("releaseDescription"),
                   email_list=dct.get("emailList"),
                   owner_id=dct.get("ownerId"),
                   attrirbutes=[ApplicationAttributeExtended.from_dict(
                        attribute,
                    )
                    for attribute in dct.get("attributes")] if dct.get("attributes") else None,  # noqa
                   business_criticality_type=BusinessCriticalityType(dct.get("businessCriticalityType")),  # noqa
                   sdlc_status_type=SdlcStatusType(dct.get("sdlcStatusType")),
                   )


class PostApplicationResponse(object):

    def __init__(self, application_id=None, success=None, errors=None):
        self.application_id = application_id
        self.success = success
        self.errors = errors

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        return cls(application_id=dct.get("application_id"),
                   success=dct.get("success"),
                   errors=dct.get("errors"))


class PostAutoReportRequest(object):

    def __init__(self,
                 static_scan_report_id=None,
                 dynamic_scan_report_id=None,
                 email_report=None,
                 report_format=None,
                 email_notification_list=None,
                 project_sdlc_status_types=None,
                 ):
        self.static_scan_report_id = static_scan_report_id
        self.dynamic_scan_report_id = dynamic_scan_report_id
        self.email_report = email_report
        self.report_format = report_format
        self.email_notification_list = email_notification_list
        self.project_sdlc_status_types = project_sdlc_status_types

    def to_dict(self):
        return dict(staticScanReportId=self.static_scan_report_id,
                    dynamicScanReportId=self.dynamic_scan_report_id,
                    emailReport=self.email_report,
                    reportFormat=self.report_format.value,
                    emailNotificationList=self.email_notification_list,
                    projectSDLCStatusTypes=self.project_sdlc_status_types,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(static_scan_report_id=dct.get("staticScanReportId"),
                   dynamic_scan_report_id=dct.get("dynamicScanReportId"),
                   email_report=dct.get("emailReport"),
                   report_format=ReportFormat(dct.get("reportFormat")) if dct.get("reportFormat") else None,  # noqa
                   email_notification_list=dct.get("emailNotificationList"),
                   project_sdlc_status_types=dct.get("projectSDLCStatusTypes"),
                   )


class PostAutoReportResponse(SuccessAndErrorsResponse):

    def __init__(self, success=None, errors=None):
        super(self.__class__, self).__init__(success=success, errors=errors)


class ReportFormat(Enum):
    """
    Enum class which represents report format. It is used for making
    application request.
    """
    HTML = "Html"
    PDF = "Pdf"


class SdlcStatusType(Enum):
    """
    Enum class which represents SDLC Status Type. It is used for making
    application request.
    """
    DEVELOPMENT = "Development"
    PRODUCTION = "Production"
    QA = "QA"
    RETIRED = "Retired"
