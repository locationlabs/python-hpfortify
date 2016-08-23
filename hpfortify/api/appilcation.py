from requests import get

from hpfortify.model.application import ApplicationListResponse
from hpfortify.model.release import ReleaseListResponse
from hpfortify.api.util import (
    get_authorization_header
)
APPLICATION_URL = "/api/v3/applications"
RELEASES_URL = "/api/v3/applications/{application_id}/releases"


def get_applications(base_url, access_token):
    """
    This method fetches all application allowed for given access token.

    :param base_url: Base url of HPfortify api.
    :type base_url: string
    :param access_token: Access token which is required for making api call.
    :type access_token: string
    """
    response = get(base_url + APPLICATION_URL,
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return ApplicationListResponse.from_dict(response.json())


def get_releases_for_application(base_url, access_token, application_id):
    """
    This method fetches the releases associated with the given application.

    :param base_url: Base url of HPfority api.
    :type base_url: string
    :param access_token: Access token to make api call.
    :type access_token: string
    :param application_id: Application id to retrieve related releases.
    :type application: integer
    """
    response = get(base_url + RELEASES_URL.format(application_id=application_id),  # noqa
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return ReleaseListResponse.from_dict(response.json())
