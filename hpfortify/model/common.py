"""
This module contains the common model classes.
"""
# Constants
ASSESSMENT_TYPE_ID = 163  # Mobile static scan


class Error(object):

    def __init__(self, error_code=None, message=None):
        self.error_code = error_code
        self.message = message

    def to_dict(self):
        return dict(errorCode=self.error_code, message=self.message)

    @classmethod
    def from_dict(cls, dct):
        return cls(error_code=dct.get("errorCode"), message=dct.get("message"))


class ErrorResponse(object):

    def __init__(self, errors=None):
        self.errors = errors

    def to_dict(self):
        return dict(errors=self.errors)

    @classmethod
    def from_dict(cls, dct):
        return cls(errors=dct.get("errors"))


class SuccessAndErrorsResponse(object):
    def __init__(self, success=None, errors=None):
        self.success = success
        self.errors = errors

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        return cls(success=dct.get("success"), errors=dct.get("errors"))
