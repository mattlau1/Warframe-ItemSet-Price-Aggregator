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
**Last Updated:** 2026-04-17 13:07 UTC

| Item Set | Median Price |
| :--- | :--- |
| Kronen Prime Set | 95p |
| Vectis Prime Set | 90p |
| Limbo Prime Set | 90p |
| Voruna Prime Set | 81p |
| Kogake Prime Set | 80p |
| Titania Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Vauban Prime Set | 80p |
| Carmine Penta Set | 80p |
| Chroma Prime Set | 77p |
| Afuris Prime Set | 77p |
| Hydroid Prime Set | 75p |
| Rhino Prime Set | 75p |
| Wukong Prime Set | 75p |
| Xiphos Set | 75p |
| Nekros Prime Set | 73p |
| Mirage Prime Set | 72p |
| Hespar Set | 72p |
| Carrier Prime Set | 70p |
| Akstiletto Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Nyx Prime Set | 70p |
| Akjagara Prime Set | 70p |
| Destreza Prime Set | 67p |
| Spira Prime Set | 66p |
| Octavia Prime Set | 66p |
| Oberon Prime Set | 65p |
| Boar Prime Set | 65p |
| Boltor Prime Set | 65p |
| Ballistica Prime Set | 65p |
| Banshee Prime Set | 65p |
| Loki Prime Set | 65p |
| Corinth Prime Set | 65p |
| Nidus Prime Set | 65p |
| Frost Prime Set | 63p |
| Bonewidow Set | 63p |
| Mag Prime Set | 62p |
| Aksomati Prime Set | 62p |
| Zephyr Prime Set | 62p |
| Saryn Prime Set | 61p |
| Gara Prime Set | 61p |
| Dual Kamas Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Glaive Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Equinox Prime Set | 60p |
| Prisma Shade Set | 60p |
| Khora Prime Set | 60p |
| Cinta Set | 60p |
| Garuda Prime Set | 58p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
