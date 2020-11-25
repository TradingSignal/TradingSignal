import argparse
from argparse import Action
from typing import List
from tradingsignal.cli.arguments import data as arguments


def add_subparser(
        subparsers: Action, parents: List[argparse.ArgumentParser]
) -> None:
    """Add all data parsers.

    Args:
        subparsers: subparser we are going to attach to
        parents: Parent parsers, needed to ensure tree structure in argparse
    """
    data_parser = subparsers.add_parser(
        "data",
        conflict_handler="resolve",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Utils for market data.",
    )
    data_parser.set_defaults(func=lambda _: data_parser.print_help(None))

    data_subparsers = data_parser.add_subparsers()

    _add_data_download_parsers(data_subparsers, parents)


def _add_data_download_parsers(
        data_subparsers, parents: List[argparse.ArgumentParser]
) -> None:
    download_parser = data_subparsers.add_parser(
        "download",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Download data from exchange.",
    )

    arguments.set_download_arguments(download_parser)
    download_parser.set_defaults(func=download_data)


def download_data(args: argparse.Namespace):
    pass
