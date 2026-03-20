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
**Last Updated:** 2026-03-20 12:45 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 210p |
| Braton Vandal Set | 200p |
| Hespar Set | 110p |
| Kronen Prime Set | 90p |
| Afuris Prime Set | 85p |
| Limbo Prime Set | 81p |
| Arum Spinosa Set | 80p |
| Vauban Prime Set | 80p |
| Wukong Prime Set | 77p |
| Kogake Prime Set | 75p |
| Titania Prime Set | 75p |
| Chroma Prime Set | 75p |
| Corinth Prime Set | 73p |
| Sporothrix Set | 72p |
| Nyx Prime Set | 72p |
| Nekros Prime Set | 72p |
| Dual Kamas Prime Set | 71p |
| Rhino Prime Set | 71p |
| Mirage Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Boar Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Carmine Penta Set | 70p |
| Gara Prime Set | 70p |
| Nidus Prime Set | 68p |
| Carrier Prime Set | 66p |
| Frost Prime Set | 65p |
| Khora Prime Set | 65p |
| Akarius Prime Set | 65p |
| Latron Prime Set | 62p |
| Bo Prime Set | 62p |
| Spira Prime Set | 61p |
| Nova Prime Set | 61p |
| Mag Prime Set | 60p |
| Latron Wraith Set | 60p |
| Akstiletto Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Loki Prime Set | 60p |
| Octavia Prime Set | 60p |
| Strun Prime Set | 60p |
| Saryn Prime Set | 57p |
| Oberon Prime Set | 56p |
| Boltor Prime Set | 55p |
| Cortege Set | 55p |
| Banshee Prime Set | 55p |
| Equinox Prime Set | 55p |
| Phantasma Prime Set | 55p |
| Baruuk Prime Set | 55p |
| Hildryn Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
