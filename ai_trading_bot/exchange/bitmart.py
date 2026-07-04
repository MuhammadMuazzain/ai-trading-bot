"""Bitmart exchange subclass"""

import logging

from ai_trading_bot.exchange import Exchange
from ai_trading_bot.exchange.exchange_types import FtHas


logger = logging.getLogger(__name__)


class Bitmart(Exchange):
    """
    Bitmart exchange class. Contains adjustments needed for AI Trading Bot to work
    with this exchange.
    """

    _ft_has: FtHas = {
        "stoploss_on_exchange": False,  # Bitmart API does not support stoploss orders
        "ohlcv_candle_limit": 200,
        "trades_has_history": False,  # Endpoint doesn't seem to support pagination
    }
