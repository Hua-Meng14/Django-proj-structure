import yaml

def yaml_coerce(value: str) -> any:
    """
    Convert a string representation of a value into its corresponding Python data type using YAML parsing.
    
    Args:
        value (str): The input value to be converted.
        
    Returns:
        any: The input value converted to its corresponding Python data type if it was a string, or the original value if it was not a string.
    """
    if isinstance(value, str):
        return yaml.safe_load(f'dummy: {value}')['dummy']
    
    return value