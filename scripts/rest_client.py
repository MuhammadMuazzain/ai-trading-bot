#!/usr/bin/env python3
"""
Simple command line client into RPC commands
Can be used as an alternate to Telegram

Should not import anything from ai_trading_bot,
so it can be used as a standalone script.
"""

from ai_trading_bot_client.cli import main


if __name__ == "__main__":
    main()
