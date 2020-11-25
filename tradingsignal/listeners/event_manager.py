from typing import Dict, Union, Any, List
from tradingsignal.resolvers.listener_resolver import ListenerResolver
from tradingsignal.listeners.event_listeners import EventListener


class EventManager:
    def __init__(self, listeners_config: Union[Dict, None, Any] = None):
        self._listeners = []
        if listeners_config is not None:
            self.load_event_listener(listeners_config)

    def load_event_listener(self, listeners_config: List[Dict]):
        """Create listener by config(dict)"""
        for listener_config in listeners_config:
            event_listener = ListenerResolver.create_listener_by_config(listener_config)
            self.subscribe(event_listener)

    def subscribe(self, listener: EventListener) -> None:
        self._listeners.append(listener)

    def unsubscribe(self, listener: EventListener) -> None:
        self._listeners.remove(listener)

    def notify(self, message) -> None:
        """
        Trigger an update in each subscriber.
        """
        for listener in self._listeners:
            listener.update(message)
