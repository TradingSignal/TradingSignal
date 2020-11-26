from typing import Text, Any, Optional, Dict
from tradingsignal.listeners.event_listeners import EventListener
from tradingsignal.utils import ts_logging
from slack.web.client import WebClient
from slack.errors import SlackApiError


class SlackListener(EventListener):
    """write the results of data miner into slack"""

    def __init__(self, listener_config: Optional[Dict[Text, Any]] = {}) -> None:
        self.listener_config = listener_config
        self.slack_client = WebClient(token=listener_config.get("token"))
        self.channel = listener_config.get("channel")

    def update(self, message: Text) -> None:
        try:
            self.slack_client.chat_postMessage(channel=self.channel, text=message)
        except SlackApiError as e:
            ts_logging.error(f"Got an error: {e.response['error']}")
        except Exception as e:
            ts_logging.error(e)
