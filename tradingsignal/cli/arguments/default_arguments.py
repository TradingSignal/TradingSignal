import argparse
from typing import Text, Optional
from tradingsignal.utils import ts_logging
from tradingsignal.constants import DEFAULT_CONFIG_PATH


def add_logging_options(parser: argparse.ArgumentParser) -> None:
    """Add options to an argument parser to configure logging levels."""

    logging_arguments = parser.add_argument_group("Python Logging Options")

    # arguments for logging configuration
    logging_arguments.add_argument(
        "-v",
        "--verbose",
        help="Be verbose. Sets logging level to INFO.",
        action="store_const",
        dest="loglevel",
        const=ts_logging.INFO,
    )
    logging_arguments.add_argument(
        "-vv",
        "--debug",
        help="Print lots of debugging statements. Sets logging level to DEBUG.",
        action="store_const",
        dest="loglevel",
        const=ts_logging.DEBUG,
    )
    logging_arguments.add_argument(
        "--quiet",
        help="Be quiet! Sets logging level to WARNING.",
        action="store_const",
        dest="loglevel",
        const=ts_logging.WARNING,
    )


def add_config_param(
        parser: argparse.ArgumentParser,
        default: Optional[Text] = DEFAULT_CONFIG_PATH,
) -> None:
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default=default,
        help="Location of the configuration file; either the path to the config or its containing directory.",
    )
