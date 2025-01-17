from datetime import datetime, timezone
import re
import json
from bson import ObjectId


def snake_to_camel(snake_str):
    """Converts a snake_case string to camelCase using regular expressions."""
    # Find all occurrences of `_` followed by a lowercase letter and convert them to uppercase
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_str)


def camel_to_snake(name):
    """Converts a camelCase string to a snake_case string."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def convert_dict_s2c(obj):
    """Recursively go through the dictionary and convert all keys to camelCase."""
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            new_key = snake_to_camel(k)
            new_dict[new_key] = convert_dict_s2c(
                v)  # Recurse into sub-dictionaries
        return new_dict
    elif isinstance(obj, list):
        # Iterate through the list and convert each item
        return [convert_dict_s2c(item) for item in obj]
    elif isinstance(obj, ObjectId):
        # Convert ObjectId to string
        return str(obj)
    elif isinstance(obj, datetime):
        # Convert datetime object to string
        return obj.isoformat()[:23]+'Z'
    else:
        # Return the item as is if it's not a dictionary or list
        return obj


def convert_dict_c2s(d, exceptions={}):
    """Recursively converts dictionary keys from camelCase to snake_case with optional exceptions."""
    # Prepare a lookup for exceptions for more efficient access
    # exception_keys = {key: value for key, value in exceptions.items()}

    def recursive_convert(obj):
        """Recursively applies key conversion to dictionary objects."""
        if isinstance(obj, dict):
            new_dict = {}
            for key, value in obj.items():
                # Apply exception if the key is listed or convert it using camel_to_snake
                # new_key = exception_keys.get(key, camel_to_snake(key))
                new_key = camel_to_snake(key)
                new_dict[new_key] = recursive_convert(value)
            return new_dict
        elif isinstance(obj, list):
            # Process each item in the list recursively
            return [recursive_convert(item) for item in obj]
        else:
            # Return the object as is if it's not a dict or list
            return obj

    return recursive_convert(d)
