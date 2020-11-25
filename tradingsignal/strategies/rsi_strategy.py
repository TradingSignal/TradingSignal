from typing import Dict, Text, Any
from talib import abstract
from pandas import DataFrame
from tradingsignal.strategies.strategy import Strategy
from tradingsignal.strategies.strategy_util import cross_over, cross_under
from tradingsignal.models.action_type import ActionType


class RSIStrategy(Strategy):
    def __init__(self, strategy_config: Dict[Text, Any] = {}) -> None:
        """
        :param strategy_config:
            time_period: Calculating rsi of the close prices, with a time period.
            over_buy: The value at which this might be good to buy
            over_sell: The value at which this might be good to sell
        """
        super().__init__(strategy_config)
        self.overbought = strategy_config.get("overbought", "70")
        self.oversold = strategy_config.get("oversold", "30")
        self.time_period = strategy_config.get("time_period", "14")

    def run_algorithm(self, historical_df: DataFrame):
        """Performs an RSI analysis on the historical data

        Args:
            historical_df: A data-frame of historical OHCLV data
        Returns:
            the name of strategy, action_type: buy, sell, hold and the lastest value of rsi indicator
        """
        output = abstract.RSI(historical_df, self.time_period)
        if cross_over(output, self.oversold):
            action_type = ActionType.BUY
        elif cross_under(output, self.overbought):
            action_type = ActionType.SELL
        else:
            action_type = None

        return self.name, action_type, output[-1]
