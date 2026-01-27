# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
**Last Updated:** 2026-01-27 02:59 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 290p |
| Lato Vandal Set | 280p |
| Vauban Prime Set | 140p |
| Akstiletto Prime Set | 120p |
| Hespar Set | 115p |
| Arum Spinosa Set | 110p |
| Dual Kamas Prime Set | 100p |
| Sporothrix Set | 95p |
| Spira Prime Set | 85p |
| Nami Skyla Prime Set | 80p |
| Tekko Prime Set | 77p |
| Akbolto Prime Set | 75p |
| Limbo Prime Set | 75p |
| Afuris Prime Set | 75p |
| Wukong Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Nova Prime Set | 70p |
| Nyx Prime Set | 70p |
| Nekros Prime Set | 70p |
| Titania Prime Set | 67p |
| Kronen Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Rhino Prime Set | 65p |
| Bo Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Mirage Prime Set | 65p |
| Octavia Prime Set | 65p |
| Gara Prime Set | 65p |
| Nidus Prime Set | 65p |
| Carrier Prime Set | 62p |
| Corinth Prime Set | 62p |
| Atlas Prime Set | 61p |
| Zephyr Prime Set | 61p |
| Latron Prime Set | 60p |
| Vectis Prime Set | 60p |
| Oberon Prime Set | 60p |
| Boar Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Baza Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Xiphos Set | 60p |
| Cortege Set | 60p |
| Morgha Set | 60p |
| Strun Prime Set | 60p |
| Garuda Prime Set | 60p |
| Khora Prime Set | 60p |
| Banshee Prime Set | 58p |
| Frost Prime Set | 57p |
| Carmine Penta Set | 56p |
| Saryn Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)