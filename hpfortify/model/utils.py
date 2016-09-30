"""
This module has all the utility methods.
"""


def remove_none_value(dct):
    """
    This method removes the key whose value is None or empty string.
    """
    return dict((k, v) for k, v in dct.iteritems() if v is not None)
