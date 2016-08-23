from requests import get
from hpfortify.model.tenant_entitlement import (  # noqa
    GetTenantEntitlementResponse,
)
from hpfortify.api.util import get_authorization_header

TENANT_ENTITLEMENT_URL = "/api/v3/tenant-entitlements"


def get_tenant_entitlements(base_url, access_token):
    """
    This method fetches all the entitlement associated with the account.

    :param base_url: Base url of HPfortify api.
    :param access_token: Access token which is necessary to access the api.
    """
    response = get(base_url + TENANT_ENTITLEMENT_URL,
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return GetTenantEntitlementResponse.from_dict(response.json())
