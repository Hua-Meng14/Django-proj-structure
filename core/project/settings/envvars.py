from core.core.utils.custom_collections import deep_update
from core.core.utils.settings import get_settings_from_environment

# globals() is a dictionary of global variables

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # noqa F821
