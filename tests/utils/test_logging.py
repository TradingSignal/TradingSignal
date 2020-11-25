from tradingsignal.utils import ts_logging


def test_log():
    # Just check that logging works without raising an exception.
    ts_logging.error("test log message")
