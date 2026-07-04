"""Crypto.com exchange subclass"""

import logging

from ai_trading_bot.exchange import Exchange
from ai_trading_bot.exchange.exchange_types import FtHas


logger = logging.getLogger(__name__)


class Cryptocom(Exchange):
    """Crypto.com exchange class.
    Contains adjustments needed for AI Trading Bot to work with this exchange.
    """

    _ft_has: FtHas = {
        "ohlcv_candle_limit": 300,
    }
