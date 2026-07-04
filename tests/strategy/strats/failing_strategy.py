# The strategy which fails to load due to non-existent dependency

import nonexiting_module  # noqa

from ai_trading_bot.strategy.interface import IStrategy


class TestStrategyLegacyV1(IStrategy):
    pass
