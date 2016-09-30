from hpfortify.model.assessment import (
    ReleaseAssessmentType,
    ReleaseAssessmentTypeListResponse,
)
from hpfortify.model.scan import (
    EntitlementFrequencyType,
    ScanType,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

RELEASE_ASSESSMENT_TYPE_DICT = {
    "assessmentTypeId": 163,
    "name": "Mobile Basic Assessment ",
    "scanType": ScanType.STATIC.value,
    "scanTypeId": 123,
    "entitlementId": 234,
    "frequencyType": EntitlementFrequencyType.SUBSCRIPTION.value,
    "frequencyTypeId": 2,
    "units": 0,
    "unitsAvailable": 8,
    "subscriptionEndDate": "2017-04-16T23:59:59",
    "isRemediation": False,
    "remediationScansAvailable": 0,
}

RELEASE_ASSESSMENT_TYPE_LIST_RESPONSE_DICT = {
    "items": [RELEASE_ASSESSMENT_TYPE_DICT],
    "totalCount": 1
}


def test_release_assessment_type():
    assert_from_and_to_dict(ReleaseAssessmentType, RELEASE_ASSESSMENT_TYPE_DICT, remove_none=True)


def test_release_assessment_type_list_response():
    assert_from_and_to_dict(ReleaseAssessmentTypeListResponse,
                            RELEASE_ASSESSMENT_TYPE_LIST_RESPONSE_DICT,
                            remove_none=True)
