"""
This module contains the common model classes.
"""


class SuccessAndErrorsResponse(object):
    def __init__(self, success=None, errors=None):
        self.success = success
        self.errors = errors

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        return cls(success=dct.get("success"), errors=dct.get("errors"))
