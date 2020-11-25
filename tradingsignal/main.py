import sys
import platform
import argparse
from tradingsignal.exceptions import TradingSignalException
from tradingsignal.cli.arguments.default_arguments import add_logging_options
from tradingsignal.cli import (
    run_server,
    data,
)
from tradingsignal.utils import ts_logging
from tradingsignal import version


def create_argument_parser() -> argparse.ArgumentParser:
    """Parse all the command line arguments for starting bot."""
    parser = argparse.ArgumentParser(
        prog="trading_signal",
        description="Trading signal command line interface. ",
    )

    parser.add_argument(
        "-v", "--version",
        action="store_true",
        default=argparse.SUPPRESS,
        help="Show Trading Signal version",
    )
    parent_parser = argparse.ArgumentParser(add_help=False)
    add_logging_options(parent_parser)
    parent_parsers = [parent_parser]

    subparsers = parser.add_subparsers(help="TradingSignal commands")

    run_server.add_subparser(subparsers, parents=parent_parsers)
    data.add_subparser(subparsers, parents=parent_parsers)

    return parser


def print_version() -> None:
    """Prints version information of trading signal and python."""

    print(f"TradingSignal Version     : {version.__version__}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Operating System : {platform.platform()}")
    print(f"Python Path      : {sys.executable}")


def main() -> None:
    arg_parser = create_argument_parser()
    cmdline_arguments = arg_parser.parse_args()
    log_level = (
        cmdline_arguments.loglevel if hasattr(cmdline_arguments, "loglevel") else None
    )
    ts_logging.set_log_level(log_level)
    try:
        if hasattr(cmdline_arguments, "func"):
            cmdline_arguments.func(cmdline_arguments)
        elif hasattr(cmdline_arguments, "version"):
            print_version()
        else:
            # user has not provided a command, let's print the help
            ts_logging.error("No command specified.")
            arg_parser.print_help()
            sys.exit(1)
    except TradingSignalException as _:
        ts_logging.exception(f'{__name__} Failed to run CLI command due to an exception.')
    except KeyboardInterrupt:
        ts_logging.info('\nERROR: Interrupted by user')


if __name__ == "__main__":
    main()
