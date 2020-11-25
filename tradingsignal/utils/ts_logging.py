import sys
import logging as _logging
from logging import DEBUG
from logging import ERROR
from logging import FATAL
from logging import INFO
from logging import WARN
from logging import WARNING
from typing import Optional, Text
from tradingsignal.exceptions import InvalidParameterException
from tradingsignal.constants import DEFAULT_LOG_LEVEL, DEFAULT_ENCODING

# Don't use this directly. Use get_logger() instead.
_logger = None
SIMPLE_FORMAT = "%(asctime)s [%(levelname)s]:%(message)s"
_level_names = {
    FATAL: 'FATAL',
    ERROR: 'ERROR',
    WARN: 'WARN',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
}


def get_logger():
    """Return TS logger instance."""
    global _logger

    if _logger:
        return _logger

    logger = _logging.getLogger('tradingsignal')
    _logging_target = sys.stderr

    # Add the output handler.
    _handler = _logging.StreamHandler(_logging_target)
    _handler.setFormatter(_logging.Formatter(SIMPLE_FORMAT, None))
    logger.addHandler(_handler)
    _logger = logger
    return _logger


def log(level, msg, *args, **kwargs):
    get_logger().log(level, msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    get_logger().debug(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    get_logger().error(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    get_logger().exception(msg, *args, **kwargs)


def fatal(msg, *args, **kwargs):
    get_logger().fatal(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    get_logger().info(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    get_logger().warning(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    get_logger().warning(msg, *args, **kwargs)


def is_enabled_for(level, *args, **kwargs):
    return get_logger().isEnabledFor(level, *args, **kwargs)


def set_log_level(log_level: Optional[int] = None):
    """Sets the log level for what messages will be logged. If none is set
    a default log level will be used."""

    if not log_level:
        log_level = DEFAULT_LOG_LEVEL
        log_level = _logging.getLevelName(log_level)

    if log_level in _level_names:
        get_logger().setLevel(log_level)
    else:
        raise InvalidParameterException()


def configure_file_logging(log_file: Optional[Text]) -> None:
    """Configure logging to a file.

    Args:
        log_file: Path of log file to write to.
    """
    if not log_file:
        return

    file_handler = _logging.FileHandler(log_file, encoding=DEFAULT_ENCODING)
    file_handler.setLevel(get_logger().level)
    file_handler.setFormatter(_logging.Formatter(SIMPLE_FORMAT, None))
    get_logger().addHandler(file_handler)
