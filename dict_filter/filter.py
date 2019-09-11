import json
from collections.abc import Iterable


class JSONStructureError(ValueError):
    pass

class FilterStructureError(ValueError):
    pass


def is_list_of_ints(l):
    """Checks if 'l' is a list with only integer values"""
    return isinstance(l, list) and oops_all_ints(l)


def is_tuple_of_ints(t):
    """Checks if 't' is a tuple with only integer values"""
    return isinstance(t, tuple) and oops_all_ints(t)


def oops_all_ints(it):
    """Checks if 'it' is an iterable with only integer values"""
    if isinstance(it, Iterable):
        for i in it:
            if not isinstance(i, int):
                return False
        return True
    else:
        return False


def dict_filter(dict_or_json, filter_dict):
    """
    Filter values out of input dict_or_json using filter_dict to select keys.

     Args:
        dict_or_json: A dict or JSON sting containing one JSON object
        filter_dict: dict

    Returns:
        dict
    """

    # Figure out what's been passed in

    # Dictionary
    if isinstance(dict_or_json, dict):
        dict_to_filter = dict_or_json

    # String, possibly JSON
    elif isinstance(dict_or_json, str):

        # Don't catch any JSON decode exceptions
        dict_to_filter = json.loads(dict_or_json)

        if not isinstance(dict_to_filter, dict):
            raise JSONStructureError("JSON strings must contain a single object")

    # Start filtering!
    return recursive_filter(dict_to_filter, filter_dict)


def recursive_filter(d, _filter):
    """
    Build a dict of key->value pairs from 'd' where keys are present in 'filter'.
    Use values in 'filter' to decide what to do with values in 'd'.
    On values that are also dictionaries we call this function recursively.
    """

    return_dict = {}

    for (k, v) in d.items():
        if not k in _filter:
            continue

        filter_value = _filter[k]

        # None => Return any value
        if filter_value is None:
            return_dict[k] = v

        # List values
        elif isinstance(v, list):

            # Empty list => Return any list value
            if filter_value == []:
                return_dict[k] = v

            # List of ints => Return indexed values from list
            elif isinstance(filter_value, list) and is_list_of_ints(filter_value):
                return_dict[k] = [v[i] for i in filter_value]

        # Tuple values
        elif isinstance(v, tuple):

            # Empty list => Return any tuple value
            if filter_value == ():
                return_dict[k] = v

            # Tuple of ints => Return indexed values from tuple
            elif isinstance(filter_value, tuple) and is_tuple_of_ints(filter_value):
                return_dict[k] = (v[i] for i in filter_value)

        # Dict values
        elif isinstance(v, dict):

            # Empty dict => Return any dict value
            if filter_value == {}:
                return_dict[k] = v

            # Non-empty dict => Recurse into dict 'v' using 'filter_value' as filter
        elif isinstance(filter_value, dict):
            return_dict[k] = recursive_filter(v, filter_value)

        # Function values:
        elif callable(filter_value):
            return_dict[k] = filter_value(v)

        else:
            raise FilterStructureError(f"Bad filter value {k}->{filter_value}")


    return return_dict