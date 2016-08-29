from requests import delete, get, post

from hpfortify.model.application import (
    ApplicationListResponse,
    DeleteApplicationResponse,
    PostApplicationResponse
)
from hpfortify.model.release import (
    ReleaseListResponse,
)
from hpfortify.api.util import (
    get_authorization_header
)
APPLICATION_URL = "/api/v3/applications"
DELETE_APPLICAITON_URL = "/api/v3/applications/{application_id}"
POST_APPLICATION_URL = "/api/v3/applications"
RELEASES_URL = "/api/v3/applications/{application_id}/releases"


def delete_application(base_url, access_token, application_id):
    """
    This method deletes the application based on passed application id.

    :param base_url: Base url of HPfority api.
    :type base_url: string
    :param access_token: Access token to make api call.
    :type access_token: string
    :param application_id: Application id that will be deleted.
    :type application: integer
    """

    response = delete(base_url + DELETE_APPLICAITON_URL.format(application_id=application_id),  # noqa
                      headers=get_authorization_header(access_token))
    response.raise_for_status()
    return DeleteApplicationResponse.from_dict(response.json())


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


def get_releases_by_application(base_url, access_token, application_id):
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


def post_application(base_url, access_token, application_request):
    """
    This method creates an application and release.

    :param base_url: Base url of HPfority api.
    :type base_url: string
    :param access_token: Access token to make api call.
    :type access_token: string
    :param application_request: Application request object.
    :type application_request: hpfortify.model.application.PostApplicationRequest  # noqa
    """
    response = post(base_url + POST_APPLICATION_URL,
                    json=application_request.to_dict(),
                    headers=get_authorization_header(access_token),
                    )

    response.raise_for_status()
    return PostApplicationResponse.from_dict(response.json())


# ---------------- Utility methods ---------------------


def is_application_id_exists(application_id, application_list):
    """
    This method checks if the application id exists in the given application
    list.
    """

    if not application_id or not application_list:
        return False

    for item in application_list.items:

        if application_id == item.application_id:
            return True

    return False


def get_release_by_application_and_release_name(base_url,
                                                access_token,
                                                application_id,
                                                release_name):
    """
    This method fetches the releases with the given release name. This method
    returns hpfortify.model.release.Release object if it successfully find it.
    Otherwise it returns None.

    :param base_url: Base url of HPfority api.
    :type base_url: string
    :param access_token: Access token to make api call.
    :type access_token: string
    :param application_id: Application id to retrieve related releases.
    :type application: integer
    :param release_name: Release name which caller is looking for.
    :type release_name: string
    """
    releases = get_releases_by_application(base_url,
                                           access_token,
                                           application_id)
    if not releases.items:
        return None

    for release in releases.items:
        if release.release_name == release_name:
            return release

    return None


def get_latest_release_id(base_url, access_token, application_id):
    """
    This method fetches the latest release id associated with the
    given application and satisfies following condition:
        1. The last scan is in Completed state.
    """
    release_id = -1
    releases = get_releases_by_application(base_url,
                                           access_token,
                                           application_id)

    if not releases.items:
        return release_id

    for release in releases.items:
        if (release_id < release.release_id and
           'Completed' == release.current_analysis_status_type):
            release_id = release.release_id

    return release_id


def is_previous_release_present(base_url, access_token, application_id):
    """
    This method checks if there is already release associated with given
    application id.
    """
    releases = get_releases_by_application(base_url,
                                           access_token,
                                           application_id)

    if releases.items and releases.total_count > 0:
        return True
    else:
        return False


def print_application_name_and_id_list(application_list):
    """
    This method prints the application name and id in a list.

    :param application_list: Application list which will be displayed by
                             this method.
    :type application_list: hpfortify.model.application.ApplicationListResponse
    """
    if not application_list:
        print "Application list is empty"
        return

    for item in application_list.items:
        print "{} => {}".format(item.application_id, item.application_name)
