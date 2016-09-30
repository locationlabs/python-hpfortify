from hpfortify.model.feature import (
    TenantFeature,
    TenantFeatureListResponse,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

TENANT_FEATURE_DICT = {
    "id": 1,
    "name": "SonaType"
}

TENANT_FEATURE_LIST_RESPONSE_DICT = {
    "items": [TENANT_FEATURE_DICT],
    "totalCount": 1,
}


def test_tenant_feature():
    assert_from_and_to_dict(TenantFeature, TENANT_FEATURE_DICT)


def test_tenant_feature_list_response():
    assert_from_and_to_dict(TenantFeatureListResponse, TENANT_FEATURE_LIST_RESPONSE_DICT)
