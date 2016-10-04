from abc import ABCMeta

from requests import (
    delete,
    get,
    post,
    put,
)

BASE_URL_US = "https://api.hpfod.com"


class BaseClientApi(object):
    __metaclass__ = ABCMeta
    """
    This is the base class for all API. This contains the basic
    information and utility methods which can be used by any of the APIs.
    """
    def __init__(self,
                 base_url=BASE_URL_US,
                 api_key=None,
                 api_secret=None,
                 access_token=None,
                 custom_headers=None):

        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.set_default_header(custom_headers)

    def set_default_header(self, custom_headers=None):
        # initialize the default headers.
        self.default_headers = dict()
        self.default_headers["Accept"] = "application/json"

        if self.access_token:
            self.default_headers["Authorization"] = "Bearer {}".format(self.access_token)

        if custom_headers:
            self.default_headers.update(custom_headers)

    def riase_for_status(self, response, status_code_response_class_dict=None):
        """
        This is a helper method to check the response and raise for status if the status
        code is not 2XX.

        Args:
            status_code_response_class_dict (dict): Status code and response class dictionary. This
                will be used to raise the status code. If the status code is not present in this
                dictionary then response class's raise_for_status method will be called.
                example:
                status_code_dict = {200: GetTenantResponse}
                self.raise_for_status(response, status_code_response_class_dict=status_code_dict)
        Returns:

        """
        if not status_code_response_class_dict:
            """ If status_code_response_class_map is not provided then use the default method
            provided requests.Response object.
            """
            response.raise_for_status()
            return response

        response_cls = status_code_response_class_dict.get(response.status_code)

        if not response_cls:
            response.raise_for_status()
            return response

        return response_cls.from_dict(response.json())

    def delete_request(self,
                       api_path,
                       additional_header=None,
                       status_code_response_class_dict=None):
        """
        Method to send delete request
        """
        final_header = dict()
        final_header.update(self.default_headers)
        if additional_header:
            final_header.update(additional_header)
        response = delete(self.base_url + api_path,
                          headers=final_header)
        return self.riase_for_status(response, status_code_response_class_dict)

    def get_request(self,
                    api_path,
                    parameters=None,
                    additional_header=None,
                    status_code_response_class_dict=None):
        final_header = dict()
        final_header.update(self.default_headers)

        if additional_header:
            final_header.update(additional_header)
        response = get(self.base_url + api_path,
                       params=parameters,
                       headers=final_header)
        return self.riase_for_status(response, status_code_response_class_dict)

    def post_request(self,
                     api_path,
                     json=None,
                     data=None,
                     params=None,
                     additional_header=None,
                     status_code_response_class_dict=None):
        final_header = dict()
        final_header.update(self.default_headers)
        if additional_header:
            final_header.update(additional_header)
        response = post(self.base_url + api_path,
                        json=json,
                        data=data,
                        params=params,
                        headers=final_header)
        return self.riase_for_status(response,
                                     status_code_response_class_dict=status_code_response_class_dict)  # noqa

    def put_request(self,
                    api_path,
                    json=None,
                    params=None,
                    additional_header=None,
                    status_code_response_class_dict=None):
        final_header = dict()
        final_header.update(self.default_headers)
        if additional_header:
            final_header.update(additional_header)
        response = put(self.base_url + api_path,
                       json=json,
                       params=params,
                       headers=final_header)
        return self.riase_for_status(response,
                                     status_code_response_class_dict=status_code_response_class_dict)  # noqa
