from ai_trading_bot import __version__


def print_version_info():
    """Print version information for ai-trading-bot and its key dependencies."""
    import platform
    import sys

    import ccxt

    print(f"Operating System:\t{platform.platform()}")
    print(f"Python Version:\t\tPython {sys.version.split(' ')[0]}")
    print(f"CCXT Version:\t\t{ccxt.__version__}")
    print()
    print(f"AI Trading Bot Version:\tai-trading-bot {__version__}")
