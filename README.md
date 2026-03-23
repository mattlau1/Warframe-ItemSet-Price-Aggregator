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
**Last Updated:** 2026-03-23 16:53 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 200p |
| Braton Vandal Set | 200p |
| Hespar Set | 100p |
| Kronen Prime Set | 90p |
| Afuris Prime Set | 90p |
| Wukong Prime Set | 80p |
| Limbo Prime Set | 80p |
| Vauban Prime Set | 80p |
| Titania Prime Set | 76p |
| Rhino Prime Set | 75p |
| Chroma Prime Set | 75p |
| Nidus Prime Set | 74p |
| Nekros Prime Set | 72p |
| Sporothrix Set | 71p |
| Xiphos Set | 70p |
| Nami Skyla Prime Set | 70p |
| Mirage Prime Set | 70p |
| Gara Prime Set | 70p |
| Akjagara Prime Set | 69p |
| Arum Spinosa Set | 66p |
| Hydroid Prime Set | 65p |
| Saryn Prime Set | 65p |
| Boar Prime Set | 65p |
| Spira Prime Set | 65p |
| Khora Prime Set | 65p |
| Akbolto Prime Set | 64p |
| Carrier Prime Set | 61p |
| Dual Kamas Prime Set | 60p |
| Mag Prime Set | 60p |
| Aksomati Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Banshee Prime Set | 60p |
| Loki Prime Set | 60p |
| Nyx Prime Set | 60p |
| Nezha Prime Set | 60p |
| Octavia Prime Set | 60p |
| Carmine Penta Set | 60p |
| Strun Prime Set | 60p |
| Garuda Prime Set | 60p |
| Prisma Shade Set | 60p |
| Hildryn Prime Set | 60p |
| Akarius Prime Set | 60p |
| Akstiletto Prime Set | 59p |
| Corinth Prime Set | 59p |
| Bo Prime Set | 58p |
| Kogake Prime Set | 57p |
| Wisp Prime Set | 56p |
| Frost Prime Set | 55p |
| Panthera Prime Set | 55p |
| Valkyr Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
