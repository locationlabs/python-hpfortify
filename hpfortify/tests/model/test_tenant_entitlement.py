from hpfortify.model.tenant_entitlement import (
    GetTenantEntitlementResponse,
    TenantEntitlement,
    TenantEntitlementExtendedProperties,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

# TODO: need to put good test data.
TENANT_ENTITLEMENT_EXTENDED_PROPERTIES_DICT = {
    "assessmentTypeId": 3456,
    "frequencyTypeId": 45678,
    "frequencyType": "Test Frequency",
    "subscriptionLength": 12,
}

TENANT_ENTITLEMENT_DICT = {
    "entitlementId": 1234,
    "unitsPurchased": 40,
    "unitsConsumed": 24,
    "startDate": "2015-10-13T00:00:00",
    "endDate": "2016-10-12T23:59:59",
    "extendedProperties": TENANT_ENTITLEMENT_EXTENDED_PROPERTIES_DICT,
}


GET_TENANT_ENTITLEMENT_RESPONSE_DICT = {
    "entitlementTypeId": 1,
    "entitlementType": "Units",
    "subscriptionTypeId": 1,
    "subscriptionType": "EntitlementPeriod",
    "tenantEntitlements": [TENANT_ENTITLEMENT_DICT]
}


def test_get_tenant_entitlement_response():
    assert_from_and_to_dict(GetTenantEntitlementResponse, GET_TENANT_ENTITLEMENT_RESPONSE_DICT)


def test_tenant_entitlement():
    assert_from_and_to_dict(TenantEntitlement, TENANT_ENTITLEMENT_DICT)


def test_tenant_entitlement_extended_properties():
    assert_from_and_to_dict(TenantEntitlementExtendedProperties,
                            TENANT_ENTITLEMENT_EXTENDED_PROPERTIES_DICT)
