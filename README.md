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
**Last Updated:** 2026-03-27 20:32 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 97p |
| Kronen Prime Set | 90p |
| Limbo Prime Set | 75p |
| Xiphos Set | 75p |
| Nami Skyla Prime Set | 75p |
| Nekros Prime Set | 75p |
| Prisma Shade Set | 71p |
| Hydroid Prime Set | 70p |
| Vauban Prime Set | 70p |
| Nyx Prime Set | 70p |
| Titania Prime Set | 69p |
| Tipedo Prime Set | 67p |
| Dual Kamas Prime Set | 65p |
| Kogake Prime Set | 65p |
| Carrier Prime Set | 65p |
| Khora Prime Set | 65p |
| Chroma Prime Set | 63p |
| Rhino Prime Set | 62p |
| Mirage Prime Set | 62p |
| Vectis Prime Set | 61p |
| Akstiletto Prime Set | 61p |
| Bo Prime Set | 60p |
| Boltor Prime Set | 60p |
| Octavia Prime Set | 60p |
| Afuris Prime Set | 60p |
| Oberon Prime Set | 58p |
| Spira Prime Set | 58p |
| Loki Prime Set | 57p |
| Wyrm Prime Set | 56p |
| Frost Prime Set | 55p |
| Saryn Prime Set | 55p |
| Wukong Prime Set | 55p |
| Mag Prime Set | 55p |
| Boar Prime Set | 55p |
| Aksomati Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Nidus Prime Set | 55p |
| Ankyros Prime Set | 52p |
| Phantasma Prime Set | 52p |
| Nezha Prime Set | 51p |
| Latron Prime Set | 50p |
| Lato Vandal Set | 50p |
| Braton Vandal Set | 50p |
| Sybaris Prime Set | 50p |
| Karak Wraith Set | 50p |
| Glaive Prime Set | 50p |
| Panthera Prime Set | 50p |
| Tekko Prime Set | 50p |
| Akjagara Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
