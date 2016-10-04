from hpfortify.model.auth import (
    AuthResponse,
    ExpireAccessTokenResponse,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

AUTH_RESPONSE_DICT = {
    "access_token": "testing-access-token",
    "token_type": "bearer",
    "expires_in": 21600,
    "scope": "https://hpfod.com/tenant"
}

EXPIRE_ACCESS_TOKEN_RESPONSE_DICT = {
    "message": "Token has expired successfully"
}


def test_auth_response():
    assert_from_and_to_dict(AuthResponse, AUTH_RESPONSE_DICT)


def test_expire_access_token_response():
    assert_from_and_to_dict(ExpireAccessTokenResponse, EXPIRE_ACCESS_TOKEN_RESPONSE_DICT)
