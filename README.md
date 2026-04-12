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
**Last Updated:** 2026-04-12 16:32 UTC

| Item Set | Median Price |
| :--- | :--- |
| Voruna Prime Set | 100p |
| Vectis Prime Set | 95p |
| Kronen Prime Set | 91p |
| Hespar Set | 84p |
| Hydroid Prime Set | 77p |
| Limbo Prime Set | 77p |
| Nami Skyla Prime Set | 77p |
| Vauban Prime Set | 77p |
| Kogake Prime Set | 76p |
| Nekros Prime Set | 75p |
| Carmine Penta Set | 75p |
| Nyx Prime Set | 74p |
| Wukong Prime Set | 72p |
| Akjagara Prime Set | 71p |
| Afuris Prime Set | 71p |
| Destreza Prime Set | 70p |
| Rhino Prime Set | 70p |
| Carrier Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Titania Prime Set | 70p |
| Bonewidow Set | 70p |
| Chroma Prime Set | 70p |
| Mirage Prime Set | 70p |
| Gara Prime Set | 68p |
| Akbolto Prime Set | 67p |
| Nidus Prime Set | 67p |
| Frost Prime Set | 65p |
| Boar Prime Set | 65p |
| Akstiletto Prime Set | 65p |
| Spira Prime Set | 65p |
| Loki Prime Set | 65p |
| Octavia Prime Set | 65p |
| Scourge Prime Set | 65p |
| Khora Prime Set | 65p |
| Boltor Prime Set | 62p |
| Xiphos Set | 62p |
| Zephyr Prime Set | 61p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Corinth Prime Set | 60p |
| Prisma Shade Set | 60p |
| Perigale Prime Set | 60p |
| Banshee Prime Set | 57p |
| Mag Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Saryn Prime Set | 55p |
| Akvasto Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Imperator Vandal Set | 55p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
