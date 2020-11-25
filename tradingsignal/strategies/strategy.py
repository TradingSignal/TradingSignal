from abc import abstractmethod
from typing import List, Optional, Dict, Any, Text


class Strategy:
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    """

    def __init__(self, strategy_config: Optional[Dict[Text, Any]] = {}) -> None:
        self.strategy_config = strategy_config
        self.name = strategy_config.get("name", Strategy.__name__)

    @abstractmethod
    def run_algorithm(self, data: List):
        raise NotImplementedError("Strategy must implement the `run_algorithm` method.")
