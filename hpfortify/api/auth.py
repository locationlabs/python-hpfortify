from requests import codes
from hpfortify.api.base import (
    BaseClientApi
)
from hpfortify.model.auth import (
    AuthResponse,
    ExpireAccessTokenResponse,
    GrantType,
)
from util import (
    SCOPE
)

AUTH_URL = "/oauth/token"
EXPIRE_ACCESS_TOKEN_URL = "/oauth/retireToken"


class AuthApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(AuthApi, self).__init__(**kwargs)

    def authorize(self):
        # Need a better way to send form data.
        data = dict()
        data["scope"] = SCOPE
        data["grant_type"] = GrantType.CLIENT_CREDENTIALS.value
        data["client_id"] = self.api_key
        data["client_secret"] = self.api_secret
        result = self.post_request(AUTH_URL,
                                   data=data,
                                   status_code_response_class_dict={codes.ok: AuthResponse})

        if type(result) is AuthResponse:
            # if the result was successful then store the access token
            self.access_token = result.access_token
            # Need to set the default header again
            self.set_default_header()

        return result

    def expire_access_token(self):
        status_code_dict = {codes.ok: ExpireAccessTokenResponse}
        return self.post_request(EXPIRE_ACCESS_TOKEN_URL,
                                 status_code_response_class_dict=status_code_dict)
