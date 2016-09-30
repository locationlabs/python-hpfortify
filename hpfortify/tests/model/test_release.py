from hpfortify.model.application import SdlcStatusType
from hpfortify.model.release import (
    CategoryCount,
    CategoryRollupsResponse,
    DeleteReleaseResponse,
    PostReleaseRequest,
    PostReleaseResponse,
    PutReleaseResponse,
    ReleaseListResponse,
    Release,
)
from hpfortify.tests.test_util import assert_from_and_to_dict
from hpfortify.tests.model.test_common import (
    SUCCESS_AND_ERRORS_RESPONSE_SUCCESS_DICT,
    SUCCESS_AND_ERRORS_RESPONSE_ERRORS_DICT,
)
# TODO need to fill good test data.
CATEGORY_COUNT_DICT = {
    "category": "Some Category",
    "count": 1
}

CATEGORY_ROLLUPS_RESPONSE_DICT = {
    "items": [CATEGORY_COUNT_DICT]
}

DELETE_RELESE_RESPONSE_SUCCESS_DICT = {
    "success": True,
    "errors": None,
}

DELETE_RELESE_RESPONSE_ERROR_DICT = {
    "success": False,
    "errors": ["Error message 1"],
}

POST_RELEASE_REQUEST_DICT = {
    "applicationId": 12345,
    "releaseName": "10.0.1",
    "releaseDescription": "Test release",
    "copyState": True,
    "copyStateReleaseId ": 10345,  # They have a typo we need to pass trailing space after this key.
    "sdlcStatusType": SdlcStatusType.PRODUCTION.value,
}

POST_RELEASE_RESPONSE_SUCCESS_DICT = {
    "releaseId": 1234,
    "success": True,
    "errors": None,
}

POST_RELEASE_RESPONSE_ERROR_DICT = {
    "releaseId": None,
    "success": False,
    "errors": ["Some error"],
}

PUT_RELEASE_RESPONSE_SUCCESS_DICT = SUCCESS_AND_ERRORS_RESPONSE_SUCCESS_DICT
PUT_RELEASE_RESPONSE_ERROR_DICT = SUCCESS_AND_ERRORS_RESPONSE_ERRORS_DICT

RELEASE_DICT = {
    "releaseId": 1234,
    "releaseName": "10.0.0",
    "releaseDescription": "Test release",
    "releaseCreatedDate": "2016-10-29T23:59:36.770Z",
    "applicationId": 1034,
    "applicationName": "Test app",
    "currentAnalysisStatusTypeId": 3,
    "currentAnalysisStatusType": "Canceled",
    "rating": 5,
    "critical": 110,
    "high": 20,
    "medium": 30,
    "low": 50,
    "currentStaticScanId": 199710,
    "currentDynamicScanId": None,
    "currentMobileScanId": None,
    "staticAnalysisStatusType": "Canceled",
    "dynamicAnalysisStatusType": None,
    "mobileAnalysisStatusType": None,
    "staticAnalysisStatusTypeId": 3,
    "dynamicAnalysisStatusTypeId": None,
    "mobileAnalysisStatusTypeId": None,
    "staticScanDate": "2016-08-17T13:28:17.77",
    "dynamicScanDate": None,
    "mobileScanDate": "2016-02-18T06:27:41.53",
    "issueCount": 0,
    "isPassed": True,
    "passFailReasonTypeId": None,
    "passFailReasonType": None,
    "sdlcStatusTypeId": 1,
    "sdlcStatusType": SdlcStatusType.PRODUCTION.value
}

RELEASE_LIST_RESPONSE_DICT = {
    "items": [RELEASE_DICT],
    "totalCount": 1
}


def test_category_count():
    assert_from_and_to_dict(CategoryCount, CATEGORY_COUNT_DICT)


def test_category_roolups_response():
    assert_from_and_to_dict(CategoryRollupsResponse, CATEGORY_ROLLUPS_RESPONSE_DICT)


def test_delete_release_response():
    assert_from_and_to_dict(DeleteReleaseResponse, DELETE_RELESE_RESPONSE_SUCCESS_DICT)
    assert_from_and_to_dict(DeleteReleaseResponse, DELETE_RELESE_RESPONSE_ERROR_DICT)


def test_post_release_request():
    assert_from_and_to_dict(PostReleaseRequest, POST_RELEASE_REQUEST_DICT)


def test_post_release_response():
    assert_from_and_to_dict(PostReleaseResponse, POST_RELEASE_RESPONSE_SUCCESS_DICT)
    assert_from_and_to_dict(PostReleaseResponse, POST_RELEASE_RESPONSE_ERROR_DICT)


def test_put_release_response():
    assert_from_and_to_dict(PutReleaseResponse, PUT_RELEASE_RESPONSE_SUCCESS_DICT)
    assert_from_and_to_dict(PutReleaseResponse, PUT_RELEASE_RESPONSE_ERROR_DICT)


def test_release():
    assert_from_and_to_dict(Release, RELEASE_DICT)


def test_release_list_response():
    assert_from_and_to_dict(ReleaseListResponse, RELEASE_LIST_RESPONSE_DICT)
