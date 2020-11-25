import os
import sys
from ruamel import yaml
from ruamel.yaml import YAMLError
from typing import (
    Text,
    Optional,
    Any,
    Union,
    Dict,
)
from pathlib import Path
from tradingsignal.utils import ts_logging
from tradingsignal.exceptions import (
    YamlException,
    FileNotFoundException,
    InvalidConfigException,
)
from tradingsignal.constants import DEFAULT_CONFIG_PATH


def get_config_path(location: Optional[Text]) -> Optional[Text]:
    """Check location of the configuration file is valid and returns the path to the config.

    Args:
        location: Location of the configuration file; either the path to the config or its containing directory..

    Returns:
        the path to the config if it is valid, else `raise error and exit`.
    """
    if os.path.isdir(location):
        location = os.path.join(location, DEFAULT_CONFIG_PATH)
    if not os.path.exists(location):
        ts_logging.error("The path '{}' does not exist. ".format(location))
        sys.exit(1)

    return location


def read_file(filename: Union[Text, Path]) -> Any:
    """Read text from a file."""

    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundException(
            f"Failed to read file, " f"'{os.path.abspath(filename)}' does not exist."
        )


def read_yaml_file(file_name: Union[Path, Text]) -> Dict[Text, Any]:
    """Parses a yaml configuration file. Content needs to be a dictionary.

    Args:
        file_name: The path to the config.
    """
    stream = read_file(file_name)
    yaml_parser = yaml.YAML()

    return yaml_parser.load(stream) or {}


def read_config_file(file_name: Union[Path, Text]) -> Dict[Text, Any]:
    """
        Read a configuration from the config file.
    Args:
        file_name: The path to the config.
    """
    try:
        configuration = read_yaml_file(file_name)
    except YAMLError as e:
        raise YamlException(file_name, e)

    if configuration is None:
        return {}
    elif isinstance(configuration, dict):
        return configuration
    else:
        raise YamlException(
            file_name,
            ValueError(
                f"Tried to load configuration file '{file_name}'. "
                f"Expected a key value mapping but found a {type(configuration).__name__}"
            ),
        )


def extract_config_by_type(configuration: Dict[Text, Any], config_type: Text):
    """Extract one config by type."""
    if config_type not in configuration:
        raise InvalidConfigException(f"Configuration is not valid. {config_type} is not found.")
    return configuration[config_type]
