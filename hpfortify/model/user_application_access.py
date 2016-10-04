"""
This module contains model class related with User Application Access.
"""
from hpfortify.model.base import (
    Resource,
    ResourceList
)


class PostUserApplicationAccessRequest(Resource):

    def __init__(self, application_id=None):
        self.application_id = application_id

    def to_dict(self):
        return dict(applicationId=self.application_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(application_id=dct.get("applicationId"))


class UserApplicationAccess(Resource):

    def __init__(self,
                 application_id=None,
                 application_name=None,
                 user_id=None,
                 access_method=None,
                 ):
        self.application_id = self.application_id
        self.application_name = application_name
        self.user_id = user_id
        self.access_method = access_method

    def to_dict(self):

        return dict(applicationId=self.application_id,
                    applicationName=self.application_name,
                    userId=self.user_id,
                    accessMethod=self.access_method,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(application_id=dct.get("applicationId"),
                   application_name=dct.get("applicationName"),
                   user_id=dct.get("userId"),
                   access_method=dct.get("accessMethod"),
                   )


class UserApplicationAccessListResponse(ResourceList):

    @classmethod
    def items_class(cls):
        return UserApplicationAccess
