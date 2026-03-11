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
**Last Updated:** 2026-03-11 05:09 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 200p |
| Braton Vandal Set | 200p |
| Dual Kamas Prime Set | 110p |
| Hespar Set | 100p |
| Kronen Prime Set | 80p |
| Corinth Prime Set | 77p |
| Hydroid Prime Set | 75p |
| Rhino Prime Set | 75p |
| Wukong Prime Set | 75p |
| Limbo Prime Set | 75p |
| Sporothrix Set | 75p |
| Chroma Prime Set | 75p |
| Vauban Prime Set | 75p |
| Nidus Prime Set | 71p |
| Kogake Prime Set | 70p |
| Nyx Prime Set | 70p |
| Mirage Prime Set | 70p |
| Gara Prime Set | 70p |
| Titania Prime Set | 68p |
| Nekros Prime Set | 68p |
| Boar Prime Set | 66p |
| Carrier Prime Set | 66p |
| Afuris Prime Set | 66p |
| Akstiletto Prime Set | 65p |
| Khora Prime Set | 65p |
| Arum Spinosa Set | 64p |
| Equinox Prime Set | 62p |
| Vectis Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Trinity Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Loki Prime Set | 60p |
| Nova Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Octavia Prime Set | 60p |
| Carmine Penta Set | 60p |
| Nezha Prime Set | 58p |
| Tekko Prime Set | 56p |
| Frost Prime Set | 55p |
| Saryn Prime Set | 55p |
| Bo Prime Set | 55p |
| Ballistica Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Wisp Prime Set | 55p |
| Akarius Prime Set | 55p |
| Revenant Prime Set | 54p |
| Akjagara Prime Set | 52p |
| Garuda Prime Set | 52p |
| Baruuk Prime Set | 52p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
