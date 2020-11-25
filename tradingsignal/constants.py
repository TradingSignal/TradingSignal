# Server
DEFAULT_SERVER_HOST = "0.0.0.0"
DEFAULT_SERVER_PORT = 8000
DEFAULT_SERVER_FORMAT = "{}://{}:{}"

# Log
DEFAULT_LOG_LEVEL_LIBRARIES = "ERROR"
ENV_LOG_LEVEL_LIBRARIES = "LOG_LEVEL_LIBRARIES"
DEFAULT_LOG_LEVEL = "INFO"

DEFAULT_ENCODING = "utf-8"

# Trading signal
DEFAULT_CONFIG_PATH = "config.yml"
TIME_FRAME = "H1"


# Config
class ConfigType:
    EXCHANGE_TYPE = "exchanges"
    LISTENER_TYPE = "listeners"
    STRATEGY_TYPE = "strategies"


# Config
class ListenerName:
    LOGGING_LISTENER = "logginglistener"
