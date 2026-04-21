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
**Last Updated:** 2026-04-21 20:44 UTC

| Item Set | Median Price |
| :--- | :--- |
| Xiphos Set | 100p |
| Hespar Set | 92p |
| Vectis Prime Set | 85p |
| Vauban Prime Set | 82p |
| Kogake Prime Set | 80p |
| Limbo Prime Set | 80p |
| Afuris Prime Set | 80p |
| Nekros Prime Set | 78p |
| Hydroid Prime Set | 77p |
| Nyx Prime Set | 75p |
| Voruna Prime Set | 75p |
| Wukong Prime Set | 72p |
| Akstiletto Prime Set | 72p |
| Corinth Prime Set | 72p |
| Aksomati Prime Set | 71p |
| Titania Prime Set | 71p |
| Ballistica Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Chroma Prime Set | 70p |
| Carmine Penta Set | 70p |
| Nidus Prime Set | 70p |
| Khora Prime Set | 70p |
| Akbolto Prime Set | 69p |
| Akjagara Prime Set | 69p |
| Rhino Prime Set | 68p |
| Gara Prime Set | 68p |
| Saryn Prime Set | 65p |
| Spira Prime Set | 65p |
| Kronen Prime Set | 65p |
| Mirage Prime Set | 65p |
| Prisma Shade Set | 61p |
| Frost Prime Set | 60p |
| Mag Prime Set | 60p |
| Strun Wraith Set | 60p |
| Carrier Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Bonewidow Set | 60p |
| Cortege Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Octavia Prime Set | 60p |
| Garuda Prime Set | 60p |
| Cinta Set | 60p |
| Tekko Prime Set | 57p |
| Sybaris Prime Set | 56p |
| Nezha Prime Set | 56p |
| Helios Prime Set | 55p |
| Bo Prime Set | 55p |
| Nikana Prime Set | 55p |
| Banshee Prime Set | 55p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
