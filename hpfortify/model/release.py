from enum import Enum

from hpfortify.model.common import SuccessAndErrorsResponse


class CategoryCount(object):

    def __init__(self, category=None, count=None):
        self.category = category
        self.count = count

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        return cls(category=dct.get("category"),
                   count=dct.get("count"),
                   )


class CategoryRollupsResponse(object):

    def __init__(self, items=None):
        self.items = items

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None)  # noqa

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[CategoryCount.from_dict(item) for item in dct.get("items")] if dct.get("items") else None)  # noqa


class DeleteReleaseResponse(SuccessAndErrorsResponse):

    def __init__(self, success=None, errors=None):
        super(self.__class__, self).__init__(success=success, errors=errors)


class PostReleaseRequest(object):
    """
    Model class to post release request
    """
    def __init__(self,
                 application_id=None,
                 release_name=None,
                 release_description=None,
                 copy_state=None,
                 copy_state_release_id=None,
                 sdlc_status_type=None,
                 ):
        self.application_id = application_id
        self.release_name = release_name
        self.release_description = release_description
        self.copy_state = copy_state
        self.copy_state_release_id = copy_state_release_id
        self.sdlc_status_type = sdlc_status_type

    def to_dict(self):
        dct = dict(applicationId=self.application_id,
                   releaseName=self.release_name,
                   releaseDescription=self.release_description,
                   copyState=self.copy_state,
                   sdlcStatusType=self.sdlc_status_type,
                   )
        # They have a typo we need to pass trailing space after this key.
        dct["copyStateReleaseId "] = self.copy_state_release_id

        return dct

    @classmethod
    def from_dict(cls, dct):
        return cls(application_id=dct.get("applicationId"),
                   release_name=dct.get("releaseName"),
                   release_description=dct.get("releaseDescription"),
                   copy_state=dct.get("copyState"),
                   copy_state_release_id=dct.get("copyStateReleaseId "),
                   sdlc_status_type=dct.get("sdlcStatusType"),
                   )


class PostReleaseResponse(object):

    def __init__(self,
                 release_id=None,
                 success=None,
                 errors=None,
                 ):
        self.release_id = release_id
        self.success = success
        self.errors = errors

    def __str__(self):
        return "<PostReleaseResponse release_id: '{}', "\
               "success: '{}', errors: '{}>".format(self.release_id,
                                                    self.success,
                                                    self.errors,
                                                    )

    def to_dict(self):
        return dict(releaseId=self.release_id,
                    success=self.success,
                    errors=self.errors,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(release_id=dct.get("releaseId"),
                   success=dct.get("success"),
                   errors=dct.get("errors"),
                   )


class PutReleaseResponse(SuccessAndErrorsResponse):

    def __init__(self, success=None, errors=None):
        super(self.__class__, self).__init__(success=success, errors=errors)


class ReleaseListResponse(object):

    def __init__(self,
                 items=None,
                 total_count=None,
                 ):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,  # noqa
                    totalCount=self.total_count,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[Release.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                   total_count=dct.get("totalCount"),
                   )


class Release(object):

    def __init__(self,
                 release_id=None,
                 release_name=None,
                 release_description=None,
                 release_create_date=None,
                 application_id=None,
                 application_name=None,
                 current_analysis_status_type_id=None,
                 current_analysis_status_type=None,
                 rating=None,
                 critical=None,
                 high=None,
                 medium=None,
                 low=None,
                 current_static_scan_id=None,
                 current_dynamic_scan_id=None,
                 current_mobile_scan_id=None,
                 static_analysis_status_type=None,
                 dynamic_analysis_status_type=None,
                 mobile_analysis_status_type=None,
                 static_analysis_status_type_id=None,
                 dynamic_analysis_status_type_id=None,
                 mobile_analysis_status_type_id=None,
                 static_scan_date=None,
                 mobile_scan_date=None,
                 dynamic_scan_date=None,
                 issue_count=None,
                 is_passed=None,
                 pass_fail_response_type_id=None,
                 pass_fail_response_type=None,
                 sdlc_status_type_id=None,
                 sdlc_status_type=None,
                 ):
        self.release_id = release_id
        self.release_name = release_name
        self.release_description = release_description
        self.release_create_date = release_create_date
        self.application_id = application_id
        self.application_name = application_name
        self.current_analysis_status_type_id = current_analysis_status_type_id
        self.current_analysis_status_type = current_analysis_status_type
        self.rating = rating
        self.critical = critical
        self.high = high
        self.medium = medium
        self.low = low
        self.current_static_scan_id = current_static_scan_id
        self.current_dynamic_scan_id = current_dynamic_scan_id
        self.current_mobile_scan_id = current_mobile_scan_id
        self.static_analysis_status_type = static_analysis_status_type
        self.dynamic_analysis_status_type = dynamic_analysis_status_type
        self.mobile_analysis_status_type = mobile_analysis_status_type
        self.static_analysis_status_type_id = static_analysis_status_type_id
        self.dynamic_analysis_status_type_id = static_analysis_status_type_id
        self.mobile_analysis_status_type_id = mobile_analysis_status_type_id
        self.static_scan_date = static_scan_date
        self.mobile_scan_date = mobile_scan_date
        self.dynamic_scan_date = dynamic_scan_date
        self.issue_count = issue_count
        self.is_passed = is_passed
        self.pass_fail_response_type_id = pass_fail_response_type_id
        self.pass_fail_response_type = pass_fail_response_type
        self.sdlc_status_type_id = sdlc_status_type_id
        self.sdlc_status_type = sdlc_status_type

    def to_dict(self):
        return dict(releaseId=self.release_id,
                    releaseName=self.release_name,
                    releaseDescription=self.release_description,
                    releaseCreatedDate=self.release_create_date,
                    applicationId=self.application_id,
                    applicationName=self.application_name,
                    currentAnalysisStatusTypeId=self.current_analysis_status_type_id,  # noqa
                    currentAnalysisStatusType=self.current_analysis_status_type,  # noqa
                    rating=self.rating,
                    critical=self.critical,
                    high=self.high,
                    medium=self.medium,
                    low=self.low,
                    currentStaticScanId=self.current_static_scan_id,
                    currentDynamicScanId=self.current_dynamic_scan_id,
                    currentMobileScanId=self.current_mobile_scan_id,
                    staticAnalysisStatusType=self.static_analysis_status_type,
                    dynamicAnalysisStatusType=self.dynamic_analysis_status_type,  # noqa
                    mobileAnalysisStatusType=self.mobile_analysis_status_type,
                    staticScanDate=self.static_scan_date,
                    dynamicScanDate=self.dynamic_scan_date,
                    mobileScanDate=self.mobile_scan_date,
                    issueCount=self.issue_count,
                    isPassed=self.is_passed,
                    passFailReasonTypeId=self.pass_fail_response_type_id,
                    passFailReasonType=self.pass_fail_response_type,
                    sdlcStatusTypeId=self.sdlc_status_type_id,
                    sdlcStatusType=self.sdlc_status_type,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(release_id=dct.get("releaseId"),
                   release_name=dct.get("releaseName"),
                   release_description=dct.get("releaseDescription"),
                   release_create_date=dct.get("releaseCreatedDate"),
                   application_id=dct.get("applicationId"),
                   application_name=dct.get("applicationName"),
                   current_analysis_status_type_id=dct.get("currentAnalysisStatusTypeId"),  # noqa
                   current_analysis_status_type=dct.get("currentAnalysisStatusType"),  # noqa
                   rating=dct.get("rating"),
                   critical=dct.get("critical"),
                   high=dct.get("high"),
                   medium=dct.get("medium"),
                   low=dct.get("low"),
                   current_static_scan_id=dct.get("currentStaticScanId"),
                   current_dynamic_scan_id=dct.get("currentDynamicScanId"),
                   current_mobile_scan_id=dct.get("currentMobileScanId"),
                   static_analysis_status_type=dct.get("staticAnalysisStatusType"),  # noqa
                   dynamic_analysis_status_type=dct.get("dynamicAnalysisStatusType"),  # noqa
                   mobile_analysis_status_type=dct.get("mobileAnalysisStatusType"),  # noqa
                   static_analysis_status_type_id=dct.get("staticAnalysisStatusTypeId"),  # noqa
                   dynamic_analysis_status_type_id=dct.get("dynamicAnalysisStatusTypeId"),  # noqa
                   mobile_analysis_status_type_id=dct.get("mobileAnalysisStatusTypeId"),  # noqa
                   static_scan_date=dct.get("staticScanDate"),
                   mobile_scan_date=dct.get("dynamicScanDate"),
                   dynamic_scan_date=dct.get("mobileScanDate"),
                   issue_count=dct.get("issueCount"),
                   is_passed=dct.get("isPassed"),
                   pass_fail_response_type_id=dct.get("passFailReasonTypeId"),
                   pass_fail_response_type=dct.get("passFailReasonType"),
                   sdlc_status_type_id=dct.get("sdlcStatusTypeId"),
                   sdlc_status_type=dct.get("sdlcStatusType"),
                   )
