import argparse


def set_download_arguments(parser: argparse.ArgumentParser):
    """Arguments for downloading market data directly using `tradingsignal download`."""
    parser.add_argument(
        "--pairs",
        type=str,
        default=None,
        help="the instrument to fetch candle data for",
    )
    parser.add_argument(
        "--from",
        type=str,
        default=None,
        help="The start of the time range to fetch candlesticks for.",
    )
    parser.add_argument(
        "--to",
        type=str,
        default=None,
        help="The end of the time range to fetch candlesticks for.",
    )
    parser.add_argument(
        "--granularity",
        type=str,
        default=None,
        help="The granularity of the candlesticks to fetch",
    )
