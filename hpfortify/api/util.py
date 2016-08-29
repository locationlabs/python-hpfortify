"""
Api utility modules.
"""

BASE_URL_US = "https://api.hpfod.com"
SCOPE = "https://hpfod.com/tenant"


def get_authorization_header(access_token):
    return {"Authorization": "Bearer {}".format(access_token),
            "Accept": "application/json"}
