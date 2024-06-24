import os

from .misc import yaml_coerce
"""
CORESETTINGS_IN_DOCKER = 1'
{
    'IN_DOCKER': 1
}
"""
"""
Retrieve settings from environment variables with a specific prefix and convert them to Python data types using YAML
parsing.

Args:
    prefix (str): The prefix used to filter environment variables.

Returns:
    dict: A dictionary containing the settings retrieved from environment variables with the specified prefix. The keys
    are obtained by removing the prefix from the environment variable names, and the values are the corresponding
    Python data types after YAML parsing.
"""


def get_settings_from_environment(prefix):
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
