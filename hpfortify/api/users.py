from requests import codes

from hpfortify.api.base import BaseClientApi
from hpfortify.model.common import (
    ErrorResponse,
    SuccessAndErrorsResponse,
)
from hpfortify.mode.users import (
    User,
    UserListResponse,
    PostUserRequest,
)

DELETE_USER_URL = "/api/v3/users/{user_id}"
GET_USER_BY_ID_URL = "/api/v3/users/{user_id}"
GET_USERS_URL = "/api/v3/users"
POST_USER_URL = "/api/v3/users"
PUT_USER_URL = "/api/v3/users/{user_id}"


class UsersApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(UsersApi, self).__init__(**kwargs)

    def delete_user(self, user_id):
        status_code_dict = {
            codes.ok: SuccessAndErrorsResponse,
        }

        return self.delete_request(
            DELETE_USER_URL.format(user_id=user_id),
            status_code_response_class_dict=status_code_dict,
        )

    def get_user_by_id(self, user_id):
        status_code_dict = {codes.ok: User}
        return self.get_request(GET_USER_BY_ID_URL.format(user_id=user_id),
                                status_code_response_class_dict=status_code_dict,
                                )

    def get_users(self):
        status_code_dict = {
            codes.ok: UserListResponse,
            codes.bad_request: SuccessAndErrorsResponse,
        }
        return self.get_request(GET_USERS_URL,
                                status_code_response_class_dict=status_code_dict,
                                )

    def post_user(self, post_user_request):
        status_code_dict = {
            codes.created: PostUserRequest,
            codes.unprocessable_entity: ErrorResponse,
            codes.internal_server_error: ErrorResponse,
        }

        return self.post_request(POST_USER_URL,
                                 json=post_user_request.to_dict(),
                                 status_code_response_class_dict=status_code_dict,
                                 )

    def update_user(self, put_user_request):
        status_code_dict = {
            codes.ok: SuccessAndErrorsResponse,
            codes.bad_request: ErrorResponse,
            codes.unprocessable_entity: ErrorResponse,
            codes.internal_server_error: ErrorResponse,
        }

        return self.put_request(PUT_USER_URL,
                                json=put_user_request.to_dict(),
                                status_code_response_class_dict=status_code_dict)
