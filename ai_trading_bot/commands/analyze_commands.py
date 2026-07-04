import logging
from typing import Any

from ai_trading_bot.enums import RunMode


logger = logging.getLogger(__name__)


def start_analysis_entries_exits(args: dict[str, Any]) -> None:
    """
    Start analysis script
    :param args: Cli args from Arguments()
    :return: None
    """
    from ai_trading_bot.configuration import setup_utils_configuration
    from ai_trading_bot.data.entryexitanalysis import process_entry_exit_reasons

    # Initialize configuration
    config = setup_utils_configuration(args, RunMode.BACKTEST)

    logger.info("Starting ai-trading-bot in analysis mode")

    process_entry_exit_reasons(config)
