# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/scan.yml/badge.svg)

A Python script that pulls median buy-order prices for all tradeable item sets by interfacing with the [Warframe Market](https://warframe.market/) API (v2).

This is helpful for finding rare items to potentially sell or to find rare relics in your inventory.

## Automation & Output
This script is set up to run automatically every hour via GitHub Actions.

It fetches the latest median prices and generates an `out.txt` file with the full dataset.

The top 50 results from that scan are injected directly into the [Live Market Prices](#-live-market-prices) section at the bottom of this page.

## Key Features
- **Set Filtering**: Finds all tradable item sets by checking slugs and item names.
- **Rate Limit Handling**: Uses a semaphore and sleep timers to stay under the API limit.
- **Async**: Fetches multiple prices concurrently to save time.
- **Resilient Scraping**: Implemented with asyncio semaphores and exponential backoff to handle rate limits gracefully.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator.git
cd Warframe-ItemSet-Price-Aggregator
```

### 2. Set up a Virtual Environment (Recommended)
**macOS / Linux (Bash):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
python3 -m venv .venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

Note: Due to the scraping speed, a full scan of ~400+ total items takes approximately 1 minute.

As of late 2025, the script analyses approximately 240+ tradeable item sets.

## 📈 Live Market Prices
[//]: # (PRICE_START)
**Last Updated:** 2026-05-29 21:49 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 100p |
| Hespar Set | 100p |
| Ballistica Prime Set | 76p |
| Carrier Prime Set | 76p |
| Limbo Prime Set | 76p |
| Titania Prime Set | 75p |
| Xiphos Set | 75p |
| Vauban Prime Set | 75p |
| Nekros Prime Set | 75p |
| Hydroid Prime Set | 70p |
| Corinth Prime Set | 70p |
| Nidus Prime Set | 70p |
| Scourge Prime Set | 70p |
| Akbolto Prime Set | 69p |
| Mirage Prime Set | 69p |
| Afuris Prime Set | 69p |
| Nami Skyla Prime Set | 67p |
| Latron Prime Set | 66p |
| Wukong Prime Set | 66p |
| Aksomati Prime Set | 66p |
| Akstiletto Prime Set | 66p |
| Frost Prime Set | 65p |
| Saryn Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Spira Prime Set | 65p |
| Kronen Prime Set | 65p |
| Octavia Prime Set | 65p |
| Gara Prime Set | 65p |
| Garuda Prime Set | 65p |
| Khora Prime Set | 65p |
| Boar Prime Set | 62p |
| Loki Prime Set | 61p |
| Oberon Prime Set | 60p |
| Cortege Set | 60p |
| Chroma Prime Set | 60p |
| Mesa Prime Set | 60p |
| Morgha Set | 60p |
| Tenora Prime Set | 60p |
| Nautilus Set | 59p |
| Strun Wraith Set | 58p |
| Destreza Prime Set | 56p |
| Glaive Prime Set | 56p |
| Wisp Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Baza Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Harrow Prime Set | 55p |
| Volt Prime Set | 53p |
| Nova Prime Set | 52p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
