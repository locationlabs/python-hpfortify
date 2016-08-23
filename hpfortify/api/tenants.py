from requests import get
from hpfortify.model.feature import TenantFeatureListResponse
from hpfortify.model.tenant import GetTenantResponse
from hpfortify.api.util import (
    get_authorization_header
)

TENANTS_FEATURES_URL = "/api/v3/tenants/features"
TENANTS_URL = "/api/v3/tenants"


def get_tenants(base_url, access_token):
    """
    This method fetches the tenant information for the given access token.

    :param base_url: Base url of HPfortify api.
    :type base_url: string
    :param access_token: Access token which is required for making api call.
    :type access_token: string
    """
    response = get(base_url + TENANTS_URL,
                   headers=get_authorization_header(access_token))

    response.raise_for_status()
    return GetTenantResponse.from_dict(response.json())


def get_tenants_features(base_url, access_token):
    """
    This method fetches the tenant information for the given access token.

    :param base_url: Base url of HPfortify api.
    :type base_url: string
    :param access_token: Access token which is required for making api call.
    :type access_token: string
    """
    response = get(base_url + TENANTS_FEATURES_URL,
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return TenantFeatureListResponse.from_dict(response.json())
