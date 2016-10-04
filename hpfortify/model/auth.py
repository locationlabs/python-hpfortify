from enum import Enum


class AuthResponse(object):
    def __init__(self,
                 access_token=None,
                 token_type=None,
                 expires_in=None,
                 scope=None):
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.scope = scope

    def to_dict(self):
        return dict(access_token=self.access_token,
                    token_type=self.token_type,
                    expires_in=self.expires_in,
                    scope=self.scope)

    @classmethod
    def from_dict(cls, dct):
        return cls(access_token=dct.get("access_token"),
                   token_type=dct.get("token_type"),
                   expires_in=dct.get("expires_in"),
                   scope=dct.get("scope"))

    def __str__(self):
        return ("<AuthResponse access_token: '{access_token}' "
                "token_type: '{token_type}' expires_in: '{expires_in}' "
                "scope: '{scope}'>".format(**self.__dict__))


class ExpireAccessTokenResponse(object):

    def __init__(self, message):
        self.message = message

    def to_dict(self):
        return dict(message=self.message)

    @classmethod
    def from_dict(cls, dct):
        return cls(message=dct.get("message"))

    def __str__(self):
        return "<ExpireAccessTokenResponse message: '{}''>".format(self.message)


class GrantType(Enum):
    """
    Enum class for Grant type
    """
    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"
