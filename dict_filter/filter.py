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


def call_filter(to_call, value, base):
    """
    Encapsulates the logic for handling callables in the filter.
    Call the callable to_call with value and possibly base.
    """

    # Callables can take either one or two values
    try:
        return to_call(value, base)
    except TypeError:
        return to_call(value)



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
    return recursive_filter(dict_to_filter, filter_dict, dict_to_filter)


def recursive_filter(d, _filter, base):
    """
    Build a dict of key->value pairs from 'd' where keys are present in 'filter'.
    Use values in 'filter' to decide what to do with values in 'd'.
    On values that are also dictionaries we call this function recursively.
    """

    return_dict = {}

    for (k, filter_value) in _filter.items():

        # If the key in the filter doesn't match anything in the dictionary,
        # check if we can call a function. Otherwise keep going.
        v = d.get(k)
        
        if not k in d:
            if callable(filter_value):
                return_dict[k] = call_filter(filter_value, v, base)
            else:
                continue

        # None => Return any value
        if filter_value is None:
            return_dict[k] = v

        # Function filter:
        elif callable(filter_value):
            return_dict[k] = call_filter(filter_value, v, base)


        # List cases
        # Empty list => Return any list value
        elif filter_value == [] and isinstance(v, list):
            return_dict[k] = v

        # List of ints => Return indexed values from list
        elif isinstance(filter_value, list) and isinstance(v, list):
            if not is_list_of_ints(filter_value):
                raise FilterStructureError(f"Bad filter value {k}->{filter_value}: List must contain 0 or more integer index values only")

            return_dict[k] = [v[i] for i in filter_value]


        # Tuple cases
        # Empty list => Return any tuple value
        elif filter_value == () and isinstance(v, tuple):
            return_dict[k] = v

        # Tuple of ints => Return indexed values from tuple
        elif isinstance(filter_value, tuple) and isinstance(v, tuple):
            if not is_tuple_of_ints(filter_value):
                raise FilterStructureError(f"Bad filter value {k}->{filter_value}: Tuple must contain 0 or more integer index values only")

            return_dict[k] = tuple(v[i] for i in filter_value)


        # Dict cases
        # Empty dict => Return any dict value
        elif filter_value == {} and isinstance(v, dict):
            return_dict[k] = v

        elif isinstance(filter_value, dict) and isinstance(v, dict):
            return_dict[k] = recursive_filter(v, filter_value, base)


        else:
            # TODO figure out error case
            pass

    return return_dict


__all__ = ['dict_filter', 'JSONStructureError', 'FilterStructureError']