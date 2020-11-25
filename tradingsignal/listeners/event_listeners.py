from abc import abstractmethod
from typing import Text, Union, Any, Optional, Dict


class EventListener:
    """
    Base class for any listener implementation. The listeners declares the update method.
    """

    def __init__(self, listener_config: Optional[Dict[Text, Any]] = None) -> None:
        self.listener_config = listener_config

    @abstractmethod
    def update(self, message: Union[Text, Any]) -> None:
        """
        Receive update from data miner.
        """
        raise NotImplementedError("Listener must implement the `update` method.")
