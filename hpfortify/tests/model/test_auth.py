from hpfortify.model.auth import (
    AuthResponse,
    ExpireAccessTokenResponse,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

# TODO need to put more meaningful data here.
AUTH_RESPONSE_DICT = {
    "access_token": "access-token-testing",
    "token_type": "token-type",
    "expires_in": "12/03/2016",
    "scope": "test-scope"
}

EXPIRE_ACCESS_TOKEN_RESPONSE_DICT = {
    "message": "Token has expired successfully"
}


def test_auth_response():
    assert_from_and_to_dict(AuthResponse, AUTH_RESPONSE_DICT)


def test_expire_access_token_response():
    assert_from_and_to_dict(ExpireAccessTokenResponse, EXPIRE_ACCESS_TOKEN_RESPONSE_DICT)
