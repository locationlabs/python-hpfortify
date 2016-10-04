from hpfortify.model.tenant import GetTenantResponse
from hpfortify.tests.test_util import assert_from_and_to_dict

GET_TENANT_RESPONE_DICT = {
    "tenantName": "location labs",
    "tenantCode": "locationlabs",
    "timeZone": "Pacific Standard Time"
}


def test_get_tenant_response():
    assert_from_and_to_dict(GetTenantResponse, GET_TENANT_RESPONE_DICT)
