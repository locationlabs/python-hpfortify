from enum import Enum
from requests import post
from hpfortify_client.model.auth import (
    AuthResponse,
    ExpireAccessTokenResponse,
)

from util import SCOPE
from util import BASE_URL_US

AUTH_URL = "/oauth/token"
EXPIRE_ACCESS_TOKEN_URL = "/oauth/retireToken"


class GrantType(Enum):
    """
    Enum class for Grant type
    """
    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"


def authorized(base_url, api_key, api_secret):
    # Need a better way to send form data.
    data = dict()
    data["scope"] = SCOPE
    data["grant_type"] = GrantType.CLIENT_CREDENTIALS.value
    data["client_id"] = api_key
    data["client_secret"] = api_secret
    return authorized_internal(base_url, data)


def authorized_internal(base_url, data):
    response = post(base_url + AUTH_URL,
                    data=data)
    # Just make sure there is no error in the response
    response.raise_for_status()

    return AuthResponse.from_json(response.text)


def expire_access_token(base_url, access_token):
    headers = dict()
    headers["Authorization"] = "Bearer {}".format(access_token)
    response = post(base_url + EXPIRE_ACCESS_TOKEN_URL, headers=headers)
    # Just make sure there is no error in the response
    response.raise_for_status()
    return ExpireAccessTokenResponse.from_json(response.text)


def main():
    response = authorized(BASE_URL_US,
                          "5df20404-bf09-4393-8807-98f8096ed497",
                          "h+rU/W4X.49S7MyFcgWEV1fKNQlDpS")
    print response
    response = expire_access_token(BASE_URL_US, response.access_token)
    import ipdb; ipdb.set_trace()
    print response

if __name__ == "__main__":
    main()
