from typing import Dict, Text, Any
from tradingsignal.exchange.exchange import Exchange
from tradingsignal.exchange.oanda import OANDA
from tradingsignal.exceptions import ClassNotFoundException

# Define classes which could be created from config.
exchange_classes = {
    'oanda': OANDA,
}


class ExchangeResolver:
    """
    This class contains all the logic to create exchange dynamically
    """

    @staticmethod
    def create_exchange_by_config(exchange_config: Dict[Text, Any]) -> Exchange:
        """Resolves a class and calls it's create method.
        """
        exchange_name = exchange_config["name"].lower()
        if exchange_name not in exchange_classes:
            raise ClassNotFoundException("Failed to load {}.".format(exchange_name))
        return exchange_classes[exchange_name](exchange_config)
