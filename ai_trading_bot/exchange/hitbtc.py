import logging

from ai_trading_bot.exchange import Exchange
from ai_trading_bot.exchange.exchange_types import FtHas


logger = logging.getLogger(__name__)


class Hitbtc(Exchange):
    """
    Hitbtc exchange class. Contains adjustments needed for AI Trading Bot to work
    with this exchange.

    Please note that this exchange is not included in the list of exchanges
    officially supported by the AI Trading Bot development team. So some features
    may still not work as expected.
    """

    _ft_has: FtHas = {
        "ohlcv_candle_limit": 1000,
    }
