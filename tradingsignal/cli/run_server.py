import argparse
from argparse import Action
from typing import List

from tradingsignal.cli.arguments import run_server as arguments
from tradingsignal.utils.io import get_config_path, read_config_file


def add_subparser(
        subparsers: Action, parents: List[argparse.ArgumentParser]
) -> None:
    """Add all run parsers.

    Args:
        subparsers: subparser we are going to attach to
        parents: Parent parsers, needed to ensure tree structure in argparse
    """
    run_parser = subparsers.add_parser(
        "runserver",
        parents=parents,
        conflict_handler="resolve",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help="Starts a TradingSignal server.",
    )
    run_parser.set_defaults(func=run_server)

    arguments.set_run_server_arguments(run_parser)


def run_server(args: argparse.Namespace):
    """Run trading signal as a server"""
    import tradingsignal.run_server
    args.config = get_config_path(args.config)
    configuration = read_config_file(args.config)
    tradingsignal.run_server(configuration, args.port, args.log_file)
