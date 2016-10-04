from hpfortify.model.scan import (
    GetImportScanSessionIdResponse,
    GetStaticScanOptionsResponse,
    LookupItem,
    PostStartScanResponse,
    PutImportScanResponse,
    Scan,
    ScanListResponse,
    ScanOption,
    ScanType,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

# TODO Need to put good test data.
GET_IMPORT_SCAN_SESSION_ID_RESPONSE_DICT = {
    "importScanSessionId": "session id"
}

LOOKUP_ITEM_DICT = {
    "value": "test value",
    "text": "test text",
    "group": "Test group"
}

POST_START_SCAN_RESPONSE_DICT = {"scanId": 345}
PUT_IMPORT_SCAN_RESPONSE_DICT = {"referenceId": 456}

# TODO: need good test data.
SCAN_DICT = {
    "applicationId": 1234,
    "releaseId": 2345,
    "scanId": 3456,
    "scanTypeId": 4567,
    "scanType": ScanType.STATIC.value,
    "assessmentTypeId": 5678,
    "analysisStatusTypeId": 6789,
    "analysisStatusType": "Status type",
    "startedDateTime": "2016-02-18T06:27:41.53",
    "completedDateTime": "2016-02-18T06:27:41.53",
    "totalIssues": 50,
    "starRating": 3,
    "notes": "Test scan note",
    "isFalsePositiveChallenge": False,
    "isRemediationScan": False
}

SCAN_LIST_RESPONSE_DICT = {
    "items": [SCAN_DICT],
    "totalCount": 1,
}

SCAN_OPTION_DICT = {
    "id": 567,
    "name": "Name scan option",
    "lastSelectedOption": LOOKUP_ITEM_DICT,
    "options": [LOOKUP_ITEM_DICT]
}

GET_STATIC_SCAN_OPTIONS_RESPONSE_DICT = {
    "items": [SCAN_OPTION_DICT],
}


def test_get_import_scan_session_id_response():
    assert_from_and_to_dict(GetImportScanSessionIdResponse,
                            GET_IMPORT_SCAN_SESSION_ID_RESPONSE_DICT)


def test_get_static_scan_options_response():
    assert_from_and_to_dict(GetStaticScanOptionsResponse,
                            GET_STATIC_SCAN_OPTIONS_RESPONSE_DICT)


def test_lookup_item():
    assert_from_and_to_dict(LookupItem, LOOKUP_ITEM_DICT)


def test_post_start_scan_response():
    assert_from_and_to_dict(PostStartScanResponse, POST_START_SCAN_RESPONSE_DICT)


def test_put_import_scan_response():
    assert_from_and_to_dict(PutImportScanResponse, PUT_IMPORT_SCAN_RESPONSE_DICT)


def test_scan_option():
    assert_from_and_to_dict(ScanOption, SCAN_OPTION_DICT)


def test_scan():
    assert_from_and_to_dict(Scan, SCAN_DICT)


def test_scan_list_response():
    assert_from_and_to_dict(ScanListResponse, SCAN_LIST_RESPONSE_DICT)
