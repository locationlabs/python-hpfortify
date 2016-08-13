from json import dumps, loads


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

    def to_json(self):
        return dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = loads(json_str)
        return cls(**json_dict)

    def __str__(self):
        return ("<AuthResponse access_token: '{access_token}' "
                "token_type: '{token_type}' expires_in: '{expires_in}' "
                "scope: '{scope}'>".format(**self.__dict__))


class ExpireAccessTokenResponse(object):

    def __init__(self, message):
        self.message = message

    def to_json(self):
        return dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        return cls(**loads(json_str))

    def __str__(self):
        return "<ExpireAccessTokenResponse message: '{}''>".format(self.message)  # noqa
