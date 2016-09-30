from hpfortify.model.application import (
    Application,
    ApplicationAttributeExtended,
    ApplicationListResponse,
    ApplicationType,
    ApplicationUser,
    ApplicationUserListResponse,
    ApplicationUserPermissions,
    BusinessCriticalityType,
    DeleteApplicationResponse,
    GetApplicationUsersResponse,
    GetAutoReportResponse,
    PostApplicationRequest,
    PostApplicationResponse,
    PostAutoReportRequest,
    PostAutoReportResponse,
    ReportFormat,
    SdlcStatusType,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

EMAIL_LIST = "test1@gmail.com,test2@gmail.com"

APPLICATION_DICT = {
    "applicationId": 100,
    "applicationName": "Test application name",
    "applicationDescription": "Test application only for unit testing",
    "applicationCreatedDate": "2016-09-25T16:34:32.487Z",
    "businessCriticalityTypeId": 10,
    "businessCriticalityType": BusinessCriticalityType.HIGH.value,
    "emailList": EMAIL_LIST,
    "applicationTypeId": 123,
    "applicationType": ApplicationType.MOBILE.value,
    "attributes": None,
}

APPLICATION_ATTRIBUTE_EXTENDED_DICT = {
    "name": "Some attribute name",
    "id": 123,
    "value": "some value"
}

APPLICATION_LIST_RESPONSE_DICT = {
    "items": [APPLICATION_DICT],
    "totalCount": 1,
}

APPLICATION_USER_DICT = {
    "userId": 1234,
    "firstName": "Fname",
    "lastName": "Lname",
}

APPLICAITON_USER_LIST_DICT = {
    "items": [APPLICATION_USER_DICT],
    "totalCount": 1,
}

APPLICATION_USER_PERMISSIONS_DICT = {
    "startDynamicScan": True,
    "startMobileScan": False,
    "startStaticScan": True,
    "createRelease": True,
    "auditIssues": True,
    "challengeIssues": True,
    "editIssues": True,
    "downloadFPR": False,
}

DELETE_APPLICAITON_RESPONSE_SUCCESS_DICT = {
    "success": True,
    "errors": None
}

DELETE_APPLICAITON_RESPONSE_ERROR_DICT = {
    "success": False,
    "errors": ["Something is wrong"]
}

GET_APPLICATION_USERS_RESPONSE_DICT = {
    "applicationId": 1234,
    "users": [APPLICATION_USER_DICT]
}

GET_AUTO_REPORT_RESPONSE_DICT = {
    "staticScanReportId": 1234,
    "staticScanReportName": "test static scan report name",
    "dynamicScanReportId": 3234,
    "dynamicScanReportName": "dynamic scan report name"
}

POST_APPLICATION_REQUEST_DICT = {
    "applicationName": "Test application name",
    "applicationDescription": "Test application description",
    "applicationType": ApplicationType.MOBILE.value,
    "releaseName": "test 1.0",
    "releaseDescription": "Release description",
    "emailList": EMAIL_LIST,
    "ownerId": 1234,
    "attributes": None,
    "businessCriticalityType": BusinessCriticalityType.HIGH.value,
    "sdlcStatusType": SdlcStatusType.PRODUCTION.value,
}

POST_APPLICATION_RESPONSE_SUCCESS_DICT = {
    "applicationId": 1234,
    "success": True,
    "errors": None
}

POST_APPLICATION_RESPONSE_ERROR_DICT = {
    "applicationId": 1234,
    "success": False,
    "errors": ["Something is wrong"]
}

POST_AUTO_REPORT_REQUEST_DICT = {
    "staticScanReportId": 100,
    "dynamicScanReportId": 200,
    "emailReport": True,
    "reportFormat": ReportFormat.PDF.value,
    "emailNotificationList": EMAIL_LIST,
    "projectSDLCStatusTypes": [SdlcStatusType.PRODUCTION.value],
}

POST_AUTO_REPORT_RESPONSE_SUCCESS_DICT = {
    "success": True,
    "errors": None
}

POST_AUTO_REPORT_RESPONSE_ERROR_DICT = {
    "success": False,
    "errors": ["Something is wrong"]
}


def test_application():
    assert_from_and_to_dict(Application, APPLICATION_DICT)


def test_application_attribute_extended():
    assert_from_and_to_dict(ApplicationAttributeExtended, APPLICATION_ATTRIBUTE_EXTENDED_DICT)


def test_application_list_response():
    assert_from_and_to_dict(ApplicationListResponse, APPLICATION_LIST_RESPONSE_DICT)


def test_application_user():
    assert_from_and_to_dict(ApplicationUser, APPLICATION_USER_DICT)


def test_application_user_list_response():
    assert_from_and_to_dict(ApplicationUserListResponse, APPLICAITON_USER_LIST_DICT)


def test_application_user_permissions():
    assert_from_and_to_dict(ApplicationUserPermissions, APPLICATION_USER_PERMISSIONS_DICT)


def test_delete_application_response():
    assert_from_and_to_dict(DeleteApplicationResponse, DELETE_APPLICAITON_RESPONSE_SUCCESS_DICT)
    assert_from_and_to_dict(DeleteApplicationResponse, DELETE_APPLICAITON_RESPONSE_ERROR_DICT)


def test_get_application_users_response():
    assert_from_and_to_dict(GetApplicationUsersResponse, GET_APPLICATION_USERS_RESPONSE_DICT)


def test_get_auto_report_response():
    assert_from_and_to_dict(GetAutoReportResponse, GET_AUTO_REPORT_RESPONSE_DICT)


def test_post_application_request():
    assert_from_and_to_dict(PostApplicationRequest, POST_APPLICATION_REQUEST_DICT, remove_none=True)


def test_post_application_response():
    assert_from_and_to_dict(PostApplicationResponse, POST_APPLICATION_RESPONSE_SUCCESS_DICT)
    assert_from_and_to_dict(PostApplicationResponse, POST_APPLICATION_RESPONSE_ERROR_DICT)


def test_post_auto_report_request():
    assert_from_and_to_dict(PostAutoReportRequest, POST_AUTO_REPORT_REQUEST_DICT)


def test_post_auto_report_response():
    assert_from_and_to_dict(PostAutoReportResponse, POST_AUTO_REPORT_RESPONSE_SUCCESS_DICT)
    assert_from_and_to_dict(PostAutoReportResponse, POST_AUTO_REPORT_RESPONSE_ERROR_DICT)
