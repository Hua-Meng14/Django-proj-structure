"""
This function deep updates a base dictionary with the values from another dictionary.
It recursively traverses both dictionaries and updates the base dictionary with the values from the
update_with dictionary.
If a key in update_with dictionary already exists in the base_dict and both values are dictionaries, it recursively
updates the nested dictionaries.
If a key in update_with dictionary does not exist in the base_dict, it adds the key-value pair to the base_dict.
If a key in update_with dictionary exists in the base_dict but the value is not a dictionary, it updates the value
in the base_dict.

Parameters:
- base_dict (dict): The dictionary to be updated.
- update_with (dict): The dictionary containing the values to update the base_dict.

Returns:
- dict: The updated base dictionary after deep updating with the values from update_with dictionary.
"""


def deep_update(base_dict, update_with):
    for key, value in update_with.items():
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value
        else:
            base_dict[key] = value

    return base_dict
