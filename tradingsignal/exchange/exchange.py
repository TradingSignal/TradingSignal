from typing import Text, Optional, Dict, Any
from abc import abstractmethod


class Exchange:

    def __init__(self, exchange_config: Optional[Dict[Text, Any]] = {}) -> None:
        self.exchange_config = exchange_config
        self.available_pairs = []

    @abstractmethod
    def get_market_data(self, instrument, granularity="H1", count=1000):
        """Fetch real-time data from exchange, brokers,."""
        raise NotImplementedError("Strategy must implement the `run_algorithm` method.")
