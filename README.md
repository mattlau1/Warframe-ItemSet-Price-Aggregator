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
**Last Updated:** 2026-03-13 05:11 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 230p |
| Braton Vandal Set | 212p |
| Dual Kamas Prime Set | 110p |
| Hespar Set | 110p |
| Kronen Prime Set | 90p |
| Sporothrix Set | 90p |
| Limbo Prime Set | 81p |
| Arum Spinosa Set | 80p |
| Afuris Prime Set | 80p |
| Wukong Prime Set | 77p |
| Chroma Prime Set | 75p |
| Akbolto Prime Set | 71p |
| Nekros Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Rhino Prime Set | 70p |
| Boar Prime Set | 70p |
| Akstiletto Prime Set | 70p |
| Vauban Prime Set | 70p |
| Nyx Prime Set | 70p |
| Mirage Prime Set | 70p |
| Corinth Prime Set | 70p |
| Gara Prime Set | 70p |
| Titania Prime Set | 68p |
| Saryn Prime Set | 65p |
| Carrier Prime Set | 65p |
| Octavia Prime Set | 65p |
| Carmine Penta Set | 65p |
| Nidus Prime Set | 65p |
| Khora Prime Set | 65p |
| Frost Prime Set | 60p |
| Mag Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Bonewidow Set | 60p |
| Nova Prime Set | 60p |
| Spira Prime Set | 58p |
| Wisp Prime Set | 58p |
| Loki Prime Set | 57p |
| Grendel Prime Set | 57p |
| Scimitar Set | 56p |
| Latron Prime Set | 55p |
| Vectis Prime Set | 55p |
| Oberon Prime Set | 55p |
| Bo Prime Set | 55p |
| Panthera Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Equinox Prime Set | 55p |
| Tenora Prime Set | 55p |
| Prisma Shade Set | 55p |
| Revenant Prime Set | 55p |
| Phantasma Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
