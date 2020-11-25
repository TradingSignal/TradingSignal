from typing import Dict, Text, Any
from tradingsignal.listeners.event_listeners import EventListener
from tradingsignal.listeners.logging_listener import LoggingListener
from tradingsignal.exceptions import ClassNotFoundException

# Define classes which could be created from config.
listener_classes = {
    'logginglistener': LoggingListener,
}


class ListenerResolver:
    """
    This class contains all the logic to create listener dynamically
    """

    @staticmethod
    def create_listener_by_config(listener_config: Dict[Text, Any]) -> EventListener:
        """Resolves a class and calls it's init method.
        """
        listener_name = listener_config["name"].lower()
        if listener_name not in listener_classes:
            raise ClassNotFoundException("Failed to load {}.".format(listener_name))
        return listener_classes[listener_name](listener_config)
