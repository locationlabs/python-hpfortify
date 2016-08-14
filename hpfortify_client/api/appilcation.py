from requests import get

from hpfortify_client.api.util import (
    get_authorization_header
)
APPLICATION_URL = "/api/v3/applications"


def get_applications(base_url, access_token):
    response = get(base_url + APPLICATION_URL,
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return response
