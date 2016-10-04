import copy
from nose.tools import eq_

from hpfortify.model.utils import remove_none_value

EXPECTED_DICT = {
    "name": "user name",
    "userId": 123,
}

DICT_WITH_NONE = {
    "name": "user name",
    "userId": 123,
    "fname": None,
    "lname": None,
}

DICT_WITHOUT_NONE = copy.deepcopy(EXPECTED_DICT)


def test_remove_none_value():
    eq_(EXPECTED_DICT, remove_none_value(DICT_WITH_NONE))
    eq_(EXPECTED_DICT, remove_none_value(DICT_WITHOUT_NONE))
