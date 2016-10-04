from hpfortify.model.users import (
    User,
    UserListResponse,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

USER1_DICT = {
    "userId": 12345,
    "userName": "user1",
    "firstName": "user1 first name",
    "lastName": "user1 second name",
    "email": "user1@test.com",
    "phoneNumber": "555111200",
    "isVerified": True,
    "roleId": 2353,
    "roleName": "Security Lead",
    "isSuspended": True,
    "mustChange": False,
    "passwordNeverExpires": False
}

USER2_DICT = {
    "userId": 23456,
    "userName": "user2",
    "firstName": "user2 first name",
    "lastName": "user2 last name",
    "email": "user2@test.com",
    "phoneNumber": "5551112300",
    "isVerified": True,
    "roleId": 2356,
    "roleName": "Lead Developer",
    "isSuspended": False,
    "mustChange": False,
    "passwordNeverExpires": False
}

USER_LIST_RESPONSE_DICT = {
    "items": [USER1_DICT, USER2_DICT],
    "totalCount": 2,
}


def test_user():
    assert_from_and_to_dict(User, USER1_DICT)
    assert_from_and_to_dict(User, USER2_DICT)


def test_user_list_response():
    assert_from_and_to_dict(UserListResponse, USER_LIST_RESPONSE_DICT)
