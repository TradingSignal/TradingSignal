import uvicorn
from fastapi import FastAPI
from typing import Optional, Text, Dict, Any
from tradingsignal.service import server
from tradingsignal.utils import ts_logging
from tradingsignal.constants import ConfigType
from tradingsignal.resolvers.exchange_resolver import ExchangeResolver
from tradingsignal.data_miner import DataMiner, start_analyze
from tradingsignal.constants import (
    DEFAULT_SERVER_PORT,
    DEFAULT_SERVER_HOST,
    DEFAULT_SERVER_FORMAT,
)
from tradingsignal.utils.io import extract_config_by_type


def run_server(
        config: Dict[Text, Any],
        port: int = DEFAULT_SERVER_PORT,
        log_file: Optional[Text] = None,
):
    """Run trading signal as a server"""
    ts_logging.configure_file_logging(log_file)
    app = server.create_app()
    host = DEFAULT_SERVER_HOST
    protocol = "http"
    server_name = DEFAULT_SERVER_FORMAT.format(protocol, host, port)
    ts_logging.info(f"Starting TradingSignal server on {server_name}.")
    register_listener_event(app, config)
    uvicorn.run(app, host=host, port=port)


def register_listener_event(
        app: FastAPI,
        config: Dict[Text, Any],
):
    @app.on_event("startup")
    async def startup_event():
        """Start analyze.
        Used to be scheduled on server start"""
        ts_logging.info("Trading Signal server is up and running.")
        exchange_config = extract_config_by_type(config, ConfigType.EXCHANGE_TYPE)
        listeners_config = extract_config_by_type(config, ConfigType.LISTENER_TYPE)
        strategies_config = extract_config_by_type(config, ConfigType.STRATEGY_TYPE)
        exchange = ExchangeResolver.create_exchange_by_config(exchange_config[0])
        data_miner = DataMiner(strategies_config, listeners_config)
        await start_analyze(data_miner, None, exchange)

    @app.on_event("shutdown")
    async def shutdown_event():
        ts_logging.info("Trading Signal server is shutdown.")
