from typing import Text, Optional


class TradingSignalException(Exception):
    """Base exception class for all errors raised by Trading Signal."""


class InvalidParameterException(TradingSignalException, ValueError):
    """Raised when an invalid parameter is used."""


class InvalidConfigException(TradingSignalException, ValueError):
    """Raised when an invalid config is passed."""


class ClassNotFoundException(TradingSignalException, ModuleNotFoundError):
    """Raised when a module referenced by name can not be imported."""


class FileNotFoundException(TradingSignalException, FileNotFoundError):
    """Raised when a file, expected to exist, doesn't exist."""


class YamlException(TradingSignalException):
    """Raised if there is an error reading yaml."""

    def __init__(self, filename: Optional[Text] = None,
                 root_exception: Optional[Exception] = None, ) -> None:
        self.filename = filename
        self.root_exception = root_exception

    def __str__(self) -> Text:
        if self.filename:
            exception_text = f"Failed to read '{self.filename}'."
        else:
            exception_text = "Failed to read YAML."

        if self.root_exception:
            self.root_exception.warn = None
            self.root_exception.note = None
            exception_text += f" {self.root_exception}"

        return exception_text
