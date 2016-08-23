from requests import get, post

from hpfortify.model.release import (
    PostReleaseResponse,
    Release,
    ReleaseListResponse,
)
from hpfortify.api.util import (
    get_authorization_header
)

GET_RELEASES_URL = "/api/v3/releases"
POST_RELEASE_URL = "/api/v3/releases"
RELEASE_URL = "/api/v3/releases/{release_id}"


def get_releases(base_url, access_token):
    """
    This method returns all the releases which can be accessible for given
    access token.

    :param base_url: Base url of HPfortify api
    :param access_token: Access token which is necessary to access the api.
    """
    response = get(base_url + GET_RELEASES_URL,
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return ReleaseListResponse.from_dict(response.json())


def get_release_by_id(base_url, access_token, release_id):
    """
    This method fetches the release information for given release id.

    :param base_url: Base url of HPfortify api.
    :param access_token: Access token which is necessary to access the api.
    :param release_id: Release id whose information will be fetched.
    :type release_id: integer
    """
    response = get(base_url + RELEASE_URL.format(release_id=release_id),
                   headers=get_authorization_header(access_token))
    response.raise_for_status()
    return Release.from_dict(response.json())


def post_release(base_url, access_token, release_request):
    """
    This method post the release information.

    :param base_url: Base url of HPfortify api.
    :param access_token: Access token which is necessary to access the api.
    :param release_request: PostReleaseRequest object.
    :type release_request: hprofity_client.model.release.PostReleaseRequest
    """
    response = post(base_url + POST_RELEASE_URL,
                    json=release_request.to_dict(),
                    headers=get_authorization_header(access_token))
    response.raise_for_status
    return PostReleaseResponse.from_dict(response.json())
