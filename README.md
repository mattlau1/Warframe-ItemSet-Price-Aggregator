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
**Last Updated:** 2026-02-19 05:19 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 275p |
| Braton Vandal Set | 275p |
| Vauban Prime Set | 135p |
| Dual Kamas Prime Set | 100p |
| Xiphos Set | 100p |
| Akstiletto Prime Set | 90p |
| Sporothrix Set | 81p |
| Aksomati Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Akjagara Prime Set | 80p |
| Carmine Penta Set | 80p |
| Afuris Prime Set | 80p |
| Arum Spinosa Set | 77p |
| Hespar Set | 75p |
| Limbo Prime Set | 72p |
| Wukong Prime Set | 71p |
| Nyx Prime Set | 71p |
| Vectis Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nidus Prime Set | 70p |
| Hydroid Prime Set | 65p |
| Titania Prime Set | 65p |
| Spira Prime Set | 65p |
| Tekko Prime Set | 65p |
| Nova Prime Set | 65p |
| Corinth Prime Set | 65p |
| Nekros Prime Set | 63p |
| Kronen Prime Set | 62p |
| Rhino Prime Set | 60p |
| Oberon Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Atlas Prime Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Mirage Prime Set | 60p |
| Octavia Prime Set | 60p |
| Dethcube Prime Set | 57p |
| Khora Prime Set | 57p |
| Trinity Prime Set | 56p |
| Carrier Prime Set | 56p |
| Frost Prime Set | 55p |
| Kogake Prime Set | 55p |
| Wyrm Prime Set | 55p |
| Cortege Set | 55p |
| Equinox Prime Set | 55p |
| Scourge Prime Set | 55p |
| Saryn Prime Set | 52p |
| Bo Prime Set | 52p |
| Akarius Prime Set | 52p |
| Valkyr Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
