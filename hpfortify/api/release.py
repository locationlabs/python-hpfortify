from requests import codes

from hpfortify.api.base import BaseClientApi
from hpfortify.model.release import (
    PostReleaseResponse,
    Release,
    ReleaseListResponse,
    DeleteReleaseResponse,
)

GET_RELEASES_URL = "/api/v3/releases"
POST_RELEASE_URL = "/api/v3/releases"
RELEASE_URL = "/api/v3/releases/{release_id}"
DELETE_RELEASE_URL = "/api/v3/releases/{release_id}"


class ReleaseApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(ReleaseApi, self).__init__(**kwargs)

    def delete_release(self, release_id):
        """
        This method deletes the release.

        :param release_id: Release id
        """
        status_code_dict = {codes.ok: DeleteReleaseResponse}
        return self.delete_request(DELETE_RELEASE_URL.format(release_id=release_id),
                                   status_code_response_class_dict=status_code_dict,
                                   )

    def get_releases(self):
        """
        This method returns all the releases which can be accessible for given
        access token.
        """
        status_code_dict = {codes.ok: ReleaseListResponse}
        return self.get_request(GET_RELEASES_URL,
                                status_code_response_class_dict=status_code_dict,
                                )

    def get_release_by_id(self, release_id):
        """
        This method fetches the release information for given release id.

        :param release_id: Release id whose information will be fetched.
        :type release_id: integer
        """
        status_code_dict = {codes.ok: Release}
        return self.get_request(RELEASE_URL.format(release_id=release_id),
                                status_code_response_class_dict=status_code_dict,
                                )

    def post_release(self, release_request):
        """
        This method post the release information.

        :param release_request: PostReleaseRequest object.
        :type release_request: hprofity.model.release.PostReleaseRequest
        """
        status_code_dict = {codes.created: PostReleaseResponse}
        return self.post_request(POST_RELEASE_URL,
                                 json=release_request.to_dict(),
                                 status_code_response_class_dict=status_code_dict,
                                 )

    # -------------- Utility methods -------------------

    def is_static_scan_present(self, release_id):
        """
        This methods determines whether there is already static scan present.
        The result can be useful to determine whether next scan should be
        remediation scan or not
        """
        release = self.get_release_by_id(release_id)

        return not release or release.current_static_scan_id
