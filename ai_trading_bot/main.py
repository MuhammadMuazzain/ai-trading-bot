#!/usr/bin/env python3
"""
Main AI Trading Bot bot script.
Read the documentation to know what cli arguments you need.
"""

import logging
import sys
from typing import Any


# check min. python version
if sys.version_info < (3, 10):  # pragma: no cover  # noqa: UP036
    sys.exit("AI Trading Bot requires Python version >= 3.10")

from ai_trading_bot import __version__
from ai_trading_bot.commands import Arguments
from ai_trading_bot.constants import DOCS_LINK
from ai_trading_bot.exceptions import ConfigurationError, AI Trading BotException, OperationalException
from ai_trading_bot.loggers import setup_logging_pre
from ai_trading_bot.system import asyncio_setup, gc_set_threshold, print_version_info


logger = logging.getLogger("ai-trading-bot")


def main(sysargv: list[str] | None = None) -> None:
    """
    This function will initiate the bot and start the trading loop.
    :return: None
    """

    return_code: Any = 1
    try:
        setup_logging_pre()
        asyncio_setup()
        arguments = Arguments(sysargv)
        args = arguments.get_parsed_arg()

        # Call subcommand.
        if args.get("version") or args.get("version_main"):
            print_version_info()
            return_code = 0
        elif "func" in args:
            logger.info(f"ai-trading-bot {__version__}")
            gc_set_threshold()
            return_code = args["func"](args)
        else:
            # No subcommand was issued.
            raise OperationalException(
                "Usage of AI Trading Bot requires a subcommand to be specified.\n"
                "To have the bot executing trades in live/dry-run modes, "
                "depending on the value of the `dry_run` setting in the config, run AI Trading Bot "
                "as `ai-trading-bot trade [options...]`.\n"
                "To see the full list of options available, please use "
                "`ai-trading-bot --help` or `ai-trading-bot <command> --help`."
            )

    except SystemExit as e:  # pragma: no cover
        return_code = e
    except KeyboardInterrupt:
        logger.info("SIGINT received, aborting ...")
        return_code = 0
    except ConfigurationError as e:
        logger.error(
            f"Configuration error: {e}\n"
            f"Please make sure to review the documentation at {DOCS_LINK}."
        )
    except AI Trading BotException as e:
        logger.error(str(e))
        return_code = 2
    except Exception:
        logger.exception("Fatal exception!")
    finally:
        sys.exit(return_code)


if __name__ == "__main__":  # pragma: no cover
    main()
