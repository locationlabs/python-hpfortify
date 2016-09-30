from copy import deepcopy
from nose.tools import eq_, ok_

from hpfortify.model.utils import (
    remove_none_value,
)


def assert_from_and_to_dict(cls, dct, extras=None, out_dict=None, remove_none=False):
    """
    Assert the .from_dict() and to_dict() methods of the resource
    return the expected values based on the given dictionary.

    :param extras - If given, expects to_dict() output to be a dictionary
                    and updates it with the dictionary given.
    :param out - If given, compare the to_dict() output with this
                 parameter value.
    :param remove_none - If set then it removes none field(s) from output.
    """
    resource = cls.from_dict(dct)
    ok_(resource)
    if extras:
        # If there are any extra keys we should expect in the to_dict output
        dct = deepcopy(dct)
        dct.update(extras)

    if not out_dict:
        out_dict = dct

    if remove_none:
        out_dict = remove_none_value(out_dict)

    eq_(resource.to_dict(), out_dict)
