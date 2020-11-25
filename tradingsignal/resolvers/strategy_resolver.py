from typing import Dict, Text, Any
from tradingsignal.strategies.strategy import Strategy
from tradingsignal.strategies.rsi_strategy import RSIStrategy
from tradingsignal.exceptions import ClassNotFoundException

# Define classes which could be created from config.
strategy_classes = {
    'rsistrategy': RSIStrategy
}


class StrategyResolver:
    """
    This class contains all the logic to create strategy dynamically
    """

    @staticmethod
    def create_strategy_by_config(strategy_config: Dict[Text, Any]) -> Strategy:
        """Resolves a class and calls it's init method.
        """
        strategy_name = strategy_config["name"].lower()
        if strategy_name not in strategy_classes:
            raise ClassNotFoundException("Failed to load {}.".format(strategy_name))
        return strategy_classes[strategy_name](strategy_config)
