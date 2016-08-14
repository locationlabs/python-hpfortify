from requests import get
from util import get_authorization_header

TENANT_ENTITLEMENT_URL = "/api/v3/tenant-entitlements"


def get_tenant_entitlements(base_url, access_token):
    response = get(base_url + TENANT_ENTITLEMENT_URL,
                   headers=get_authorization_header(access_token))

    response.raise_for_status()
    return response
