from json import dumps
"""
This module has all the utility methods.
"""


def remove_none_value(dct):
    """
    This method removes the key whose value is None or empty string.
    """
    return dict((k, v) for k, v in dct.iteritems() if v is not None)


def print_response(response, message=None):
    """
    This method prints the response model object in pretty format.
    """
    if message:
        print message

    print dumps(response.to_dict(), indent=3, sort_keys=True)
