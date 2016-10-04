from hpfortify.model.common import (
    Error,
    ErrorResponse,
    SuccessAndErrorsResponse,
)
from hpfortify.tests.test_util import assert_from_and_to_dict


SUCCESS_AND_ERRORS_RESPONSE_SUCCESS_DICT = {
    "success": True,
    "errors": None
}

SUCCESS_AND_ERRORS_RESPONSE_ERRORS_DICT = {
    "success": False,
    "errors": ["Error message 1", "error message 2"]
}

# TODO: need to put good test data
ERROR_DICT = {
    "errorCode": 400,
    "message": "bad request"
}

ERROR_RESPONSE_DICT = {
    "errors": [ERROR_DICT]
}


def test_error():
    assert_from_and_to_dict(Error, ERROR_DICT)


def test_error_response():
    assert_from_and_to_dict(ErrorResponse, ERROR_RESPONSE_DICT)


def test_success_and_errors_response_success():
    assert_from_and_to_dict(SuccessAndErrorsResponse, SUCCESS_AND_ERRORS_RESPONSE_SUCCESS_DICT)


def test_success_and_errors_response_errors():
    assert_from_and_to_dict(SuccessAndErrorsResponse, SUCCESS_AND_ERRORS_RESPONSE_ERRORS_DICT)
