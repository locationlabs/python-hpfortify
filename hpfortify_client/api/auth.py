from requests import post
from hpfortify_client.model.auth import (
    AuthResponse,
    ExpireAccessTokenResponse,
    GrantType,
)
from util import (
    get_authorization_header,
    SCOPE
)

AUTH_URL = "/oauth/token"
EXPIRE_ACCESS_TOKEN_URL = "/oauth/retireToken"


def authorize(base_url, api_key, api_secret):
    # Need a better way to send form data.
    data = dict()
    data["scope"] = SCOPE
    data["grant_type"] = GrantType.CLIENT_CREDENTIALS.value
    data["client_id"] = api_key
    data["client_secret"] = api_secret
    return authorize_internal(base_url, data)


def authorize_internal(base_url, data):
    response = post(base_url + AUTH_URL,
                    data=data)
    # Just make sure there is no error in the response
    response.raise_for_status()

    return AuthResponse.from_json(response.text)


def expire_access_token(base_url, access_token):

    response = post(base_url + EXPIRE_ACCESS_TOKEN_URL,
                    headers=get_authorization_header(access_token))
    # Just make sure there is no error in the response
    response.raise_for_status()
    return ExpireAccessTokenResponse.from_json(response.text)
