from typing import Text, Union, Any, Optional, Dict
from tradingsignal.listeners.event_listeners import EventListener
from tradingsignal.utils import ts_logging


class LoggingListener(EventListener):
    """write the results of data miner into log-file"""

    def __init__(self, listener_config: Optional[Dict[Text, Any]] = {}) -> None:
        self.listener_config = listener_config

    def update(self, message: Union[Text, Any]) -> None:
        ts_logging.info(str(message))
