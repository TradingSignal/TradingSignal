from typing import List, Optional, Text
from tradingsignal.listeners.event_manager import EventManager
from tradingsignal.strategies.strategy import Strategy
from tradingsignal.resolvers.strategy_resolver import StrategyResolver
from tradingsignal.exchange.exchange import Exchange
from tradingsignal.utils import ts_logging
from tradingsignal.utils import ts_scheduler
from tradingsignal.constants import TIME_FRAME


class DataMiner:
    def __init__(
            self,
            strategies_config,
            listeners_config,
    ):
        self.events = EventManager(listeners_config)
        self.strategies: List[Strategy] = []
        self._create_strategies(strategies_config)

    def _create_strategies(self, strategies_config):
        for strategy_config in strategies_config:
            self.strategies.append(StrategyResolver.create_strategy_by_config(strategy_config))

    def analyze_data(self, data, data_name: Optional[Text] = ""):
        print(f"[{self.__class__.__name__}] I'm doing something important.")
        for _strategy in self.strategies:
            _strategy.run_algorithm(data)
            self.events.notify(message="Something has just updated")


async def schedule_analyze_data(time_between_calls: int, exchange: Exchange, data_miner: DataMiner):
    (await ts_scheduler.scheduler()).add_job(
        send_analysis_report,
        "interval",
        seconds=time_between_calls,
        args=[exchange, data_miner],
        id="analyze_data_from_exchange",
        replace_existing=True,
    )


async def send_analysis_report(exchange: Exchange, data_miner: DataMiner):
    print("make_analysis_report")
    for pair in exchange.available_pairs:
        market_df = exchange.get_market_data(pair, TIME_FRAME)
        data_miner.analyze_data(market_df, pair)


async def analyze_data_from_exchange(exchange: Exchange, data_miner: DataMiner):
    # start scheduler
    time_between_calls = 60
    await schedule_analyze_data(time_between_calls, exchange, data_miner)


async def start_analyze(
        data_miner: DataMiner,
        local_data_path: Optional[Text] = None,
        exchange: Optional[Exchange] = None,
):
    """Logic to run data miner to analyze data from local machine or real-time data from exchange"""
    if exchange is not None:
        await analyze_data_from_exchange(exchange, data_miner)
    elif local_data_path is not None:
        ts_logging.warning("run back test")
    else:
        ts_logging.warning("No valid configuration given to run")
