"""
This module contains model class related with user api.
"""


class PostUserRequest(object):

    def __init__(self,
                 user_name=None,
                 email=None,
                 first_name=None,
                 last_name=None,
                 phone_number=None,
                 role_id=None,
                 password_never_expires=None,
                 is_suspended=None,
                 ):
        self.user_name = user_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.role_id = role_id
        self.password_never_expires = password_never_expires
        self.is_suspended = is_suspended

    def to_dict(self):
        return dict(userName=self.user_name,
                    email=self.email,
                    firstName=self.first_name,
                    lastName=self.last_name,
                    phoneNumber=self.phone_number,
                    roleId=self.role_id,
                    passwordNeverExpires=self.password_never_expires,
                    isSuspended=self.is_suspended,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(user_name=dct.get("userName"),
                   email=dct.get("email"),
                   first_name=dct.get("firstName"),
                   last_name=dct.get("lastName"),
                   phone_number=dct.get("phoneNumber"),
                   role_id=dct.get("roleId"),
                   password_never_expires=dct.get("passwordNeverExpires"),
                   is_suspended=dct.get("isSuspended"),
                   )


class PutUserRequest(object):

    def __init__(self,
                 email=None,
                 first_name=None,
                 last_name=None,
                 phone_number=None,
                 role_id=None,
                 password_never_expires=None,
                 is_suspended=None,
                 must_change=None,
                 password=None,
                 ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.role_id = role_id
        self.password_never_expires = password_never_expires
        self.is_suspended = is_suspended
        self.must_change = must_change
        self.password = password

    def to_dict(self):
        return dict(email=self.email,
                    firstName=self.first_name,
                    lastName=self.last_name,
                    phoneNumber=self.phone_number,
                    roleId=self.role_id,
                    passwordNeverExpires=self.password_never_expires,
                    isSuspended=self.is_suspended,
                    mustChange=self.must_change,
                    password=self.password,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(email=dct.get("email"),
                   first_name=dct.get("firstName"),
                   last_name=dct.get("lastName"),
                   phone_number=dct.get("phoneNumber"),
                   role_id=dct.get("roleId"),
                   password_never_expires=dct.get("passwordNeverExpires"),
                   is_suspended=dct.get("isSuspended"),
                   must_change=dct.get("mustChange"),
                   password=dct.get("password"),
                   )


class PostUserResponse(object):

    def __init__(self, user_id=None):
        self.user_id = user_id

    def to_dict(self):
        return dict(userid=self.user_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(user_id=dct.get("userId"))


class User(object):

    def __init__(self,
                 user_id=None,
                 user_name=None,
                 first_name=None,
                 last_name=None,
                 email=None,
                 phone_number=None,
                 is_verified=None,
                 role_id=None,
                 role_name=None,
                 is_suspended=None,
                 must_change=None,
                 password_never_expires=None,
                 ):

        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.is_verified = is_verified
        self.role_id = role_id
        self.role_name = role_name
        self.is_suspended = is_suspended
        self.must_change = must_change
        self.password_never_expires = password_never_expires

    def to_dict(self):
        return dict(userId=self.user_id,
                    userName=self.user_name,
                    firstName=self.first_name,
                    lastName=self.last_name,
                    email=self.email,
                    phoneNumber=self.phone_number,
                    isVerified=self.is_verified,
                    roleId=self.role_id,
                    roleName=self.role_name,
                    isSuspended=self.is_suspended,
                    mustChange=self.must_change,
                    passwordNeverExpires=self.password_never_expires,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(user_id=dct.get("userId"),
                   user_name=dct.get("userName"),
                   first_name=dct.get("firstName"),
                   last_name=dct.get("lastName"),
                   email=dct.get("email"),
                   phone_number=dct.get("phoneNumber"),
                   is_verified=dct.get("isVerified"),
                   role_id=dct.get("roleId"),
                   role_name=dct.get("roleName"),
                   is_suspended=dct.get("isSuspended"),
                   must_change=dct.get("mustChange"),
                   password_never_expires=dct.get("passwordNeverExpires"),
                   )


class UserListResponse(object):

    def __init__(self, items=None, total_count=None):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,
                    totalCount=self.total_count,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[User.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                   total_count=dct.get("totalCount"))
