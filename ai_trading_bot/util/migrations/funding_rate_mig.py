import logging

from ai_trading_bot.constants import Config
from ai_trading_bot.enums import TradingMode
from ai_trading_bot.exchange import Exchange


logger = logging.getLogger(__name__)


def migrate_funding_fee_timeframe(config: Config, exchange: Exchange | None):
    from ai_trading_bot.data.history import get_datahandler

    if config.get("trading_mode", TradingMode.SPOT) != TradingMode.FUTURES:
        # only act on futures
        return

    if not exchange:
        from ai_trading_bot.resolvers import ExchangeResolver

        exchange = ExchangeResolver.load_exchange(config, validate=False)

    ff_timeframe = exchange.get_option("funding_fee_timeframe")

    dhc = get_datahandler(config["datadir"], config["dataformat_ohlcv"])
    dhc.fix_funding_fee_timeframe(ff_timeframe)
