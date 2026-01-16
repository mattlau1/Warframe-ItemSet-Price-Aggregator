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
**Last Updated:** 2026-01-16 00:50 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 315p |
| Braton Vandal Set | 307p |
| Vauban Prime Set | 120p |
| Akstiletto Prime Set | 110p |
| Arum Spinosa Set | 110p |
| Dual Kamas Prime Set | 90p |
| Akjagara Prime Set | 88p |
| Limbo Prime Set | 83p |
| Nyx Prime Set | 82p |
| Hespar Set | 82p |
| Spira Prime Set | 80p |
| Kronen Prime Set | 80p |
| Sporothrix Set | 80p |
| Nami Skyla Prime Set | 77p |
| Aksomati Prime Set | 76p |
| Afuris Prime Set | 76p |
| Tekko Prime Set | 75p |
| Nekros Prime Set | 73p |
| Carrier Prime Set | 70p |
| Valkyr Prime Set | 70p |
| Garuda Prime Set | 70p |
| Hydroid Prime Set | 67p |
| Saryn Prime Set | 67p |
| Titania Prime Set | 67p |
| Mirage Prime Set | 67p |
| Nidus Prime Set | 67p |
| Nova Prime Set | 66p |
| Carmine Penta Set | 66p |
| Frost Prime Set | 65p |
| Wukong Prime Set | 65p |
| Boar Prime Set | 65p |
| Akbolto Prime Set | 65p |
| Atlas Prime Set | 65p |
| Octavia Prime Set | 65p |
| Gara Prime Set | 65p |
| Sybaris Prime Set | 61p |
| Loki Prime Set | 61p |
| Khora Prime Set | 61p |
| Wolf Sledge Set | 60p |
| Rhino Prime Set | 60p |
| Bo Prime Set | 60p |
| Venka Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Chroma Prime Set | 60p |
| Corinth Prime Set | 60p |
| Glaive Prime Set | 58p |
| Vectis Prime Set | 57p |
| Oberon Prime Set | 55p |
| Trinity Prime Set | 55p |
| Ballistica Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)