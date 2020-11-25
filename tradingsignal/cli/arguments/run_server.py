import argparse
from typing import Union
from tradingsignal import constants
from tradingsignal.cli.arguments.default_arguments import add_config_param


def set_run_server_arguments(parser: argparse.ArgumentParser):
    """Arguments for running TradingSignal directly using `tradingsignal run_server`."""
    parser.add_argument(
        "--log-file",
        type=str,
        default=None,
        help="Store logs in specified file.",
    )

    server_arguments = parser.add_argument_group("Server Settings")

    add_port_argument(server_arguments)
    add_config_param(parser)


# noinspection PyProtectedMember
def add_port_argument(parser: Union[argparse.ArgumentParser, argparse._ArgumentGroup]):
    """Add an argument for port."""
    parser.add_argument(
        "-p",
        "--port",
        default=constants.DEFAULT_SERVER_PORT,
        type=int,
        help="Port to run the server at.",
    )
