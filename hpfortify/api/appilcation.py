from requests import codes

from hpfortify.api.base import BaseClientApi
from hpfortify.model.application import (
    ApplicationListResponse,
    DeleteApplicationResponse,
    PostApplicationResponse
)
from hpfortify.model.release import (
    ReleaseListResponse,
)

APPLICATION_URL = "/api/v3/applications"
DELETE_APPLICAITON_URL = "/api/v3/applications/{application_id}"
POST_APPLICATION_URL = "/api/v3/applications"
RELEASES_URL = "/api/v3/applications/{application_id}/releases"


class ApplicationApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(ApplicationApi, self).__init__(**kwargs)

    def delete_application(self, application_id):
        """
        This method deletes the application based on passed application id.

        :param base_url: Base url of HPfority api.
        :type base_url: string
        :param access_token: Access token to make api call.
        :type access_token: string
        :param application_id: Application id that will be deleted.
        :type application: integer
        """
        status_code_dict = {codes.ok: DeleteApplicationResponse}
        return self.delete_request(
            DELETE_APPLICAITON_URL.format(application_id=application_id),
            status_code_response_class_dict=status_code_dict,
        )

    def get_applications(self):
        """
        This method fetches all application allowed for given access token.
        """
        status_code_dict = {codes.ok: ApplicationListResponse}
        return self.get_request(APPLICATION_URL,
                                status_code_response_class_dict=status_code_dict,
                                )

    def get_releases_by_application(self, application_id):
        """
        This method fetches the releases associated with the given application.

        :param application_id: Application id to retrieve related releases.
        :type application: integer
        """
        status_code_dict = {codes.ok: ReleaseListResponse}
        return self.get_request(RELEASES_URL.format(application_id=application_id),
                                status_code_response_class_dict=status_code_dict)

    def post_application(self, application_request):
        """
        This method creates an application and release.

        :param application_request: Application request object.
        :type application_request: hpfortify.model.application.PostApplicationRequest  # noqa
        """
        status_code_dict = {codes.created: PostApplicationResponse}
        return self.post_request(POST_APPLICATION_URL,
                                 json=application_request.to_dict(),
                                 status_code_response_class_dict=status_code_dict,
                                 )

    # ---------------- Utility methods ---------------------

    def is_application_id_exists(self, application_id, application_list):
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


    def get_application_by_name(base_url, access_token, application_name):
        """
        This method fetches the application based on the application name.
        It returns Application object if it is successful. Otherwise it returns
        None.

        :param base_url: Base url of HPfority api.
        :type base_url: string
        :param access_token: Access token to make api call.
        :type access_token: string
        :param application_name: Application name to retrieve related Application.
        :type application_name: string
        """
        try:
            applications = get_applications(base_url, access_token)

            if applications.total_count <= 0:
                return None

            for application in applications.items:

                if application.application_name == application_name:
                    return application

        except Exception as error:
            print "Error: {}".format(error.strerror)
            return None


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
        :type application_id: integer
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
