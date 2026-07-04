# AI Trading Bot

**Author:** Muhammad Muazzain  
**Email:** muhammadmuazzain07@gmail.com  
**Repository:** [https://github.com/MuhammadMuazzain/ai-trading-bot](https://github.com/MuhammadMuazzain/ai-trading-bot)

AI-powered crypto trading assistant that analyzes market trends and generates buy/sell signals using real-time exchange data, technical indicators, and optional ML-based strategy optimization.

Built with Python. Supports major exchanges, backtesting, dry-run mode, Telegram/Web UI control, and strategy tuning.

---

## Disclaimer

Always start in **dry-run** mode. Do not trade with real funds until you understand the bot, your strategy, and the risks involved.

You should be comfortable reading and modifying Python code before running this in production.

---

## Features

- **Python 3.10+** — Windows, macOS, and Linux
- **Multi-exchange support** — Binance, Bybit, Kraken, OKX, Gate.io, and more via CCXT
- **Dry-run** — Test strategies without real money
- **Backtesting** — Simulate strategies on historical data
- **Strategy optimization** — Hyperopt and optional ML / AI model pipelines
- **Web UI & Telegram** — Monitor and control the bot remotely
- **Persistence** — SQLite-backed trade history

---

## Quick Start

### Clone the repository

```bash
git clone https://github.com/MuhammadMuazzain/ai-trading-bot.git
cd ai-trading-bot
```

### Install (Linux / macOS)

```bash
./setup.sh -i
```

### Install (Windows)

```powershell
.\setup.ps1
```

### Create config and run (dry-run)

```bash
ai-trading-bot create-userdir --userdir user_data
ai-trading-bot new-config
ai-trading-bot trade --config user_data/config.json --dry-run
```

See the [docs/](docs/) folder for full installation, configuration, and strategy guides.

---

## Supported Exchanges

Binance, Bitmart, BingX, Bybit, Gate.io, HTX, Hyperliquid, Kraken, OKX, and others via [CCXT](https://github.com/ccxt/ccxt/). Check [docs/exchanges.md](docs/exchanges.md) for exchange-specific notes.

---

## Project Structure

| Path | Description |
|---|---|
| `ai_trading_bot/` | Core trading engine |
| `user_data/` | Your strategies, configs, and data |
| `docs/` | Documentation |
| `config_examples/` | Sample configuration files |
| `docker/` | Docker deployment files |

---

## Requirements

- Python >= 3.10
- pip, git, TA-Lib
- Recommended: virtualenv or Docker
- Minimum cloud instance: 2 GB RAM, 1 GB disk, 2 vCPU

---

## Contact

**Muhammad Muazzain**  
muhammadmuazzain07@gmail.com  
[GitHub](https://github.com/MuhammadMuazzain/ai-trading-bot)

---

## License

Licensed under the [GNU General Public License v3.0](LICENSE).
