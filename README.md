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
**Last Updated:** 2026-03-24 01:29 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 204p |
| Braton Vandal Set | 200p |
| Hespar Set | 99p |
| Kronen Prime Set | 90p |
| Wukong Prime Set | 85p |
| Limbo Prime Set | 80p |
| Arum Spinosa Set | 80p |
| Titania Prime Set | 76p |
| Boltor Prime Set | 75p |
| Vauban Prime Set | 75p |
| Nekros Prime Set | 75p |
| Corinth Prime Set | 75p |
| Khora Prime Set | 75p |
| Afuris Prime Set | 75p |
| Nidus Prime Set | 74p |
| Rhino Prime Set | 71p |
| Gara Prime Set | 70p |
| Hydroid Prime Set | 67p |
| Dual Kamas Prime Set | 67p |
| Chroma Prime Set | 67p |
| Octavia Prime Set | 66p |
| Carmine Penta Set | 66p |
| Latron Prime Set | 65p |
| Boar Prime Set | 65p |
| Carrier Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Spira Prime Set | 65p |
| Tenora Prime Set | 65p |
| Mirage Prime Set | 63p |
| Saryn Prime Set | 61p |
| Loki Prime Set | 61p |
| Vectis Prime Set | 60p |
| Akstiletto Prime Set | 60p |
| Nyx Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Equinox Prime Set | 60p |
| Strun Prime Set | 60p |
| Scourge Prime Set | 60p |
| Garuda Prime Set | 60p |
| Prisma Shade Set | 60p |
| Wisp Prime Set | 60p |
| Revenant Prime Set | 58p |
| Baza Prime Set | 57p |
| Mag Prime Set | 56p |
| Centaur Set | 56p |
| Hildryn Prime Set | 56p |
| Frost Prime Set | 55p |
| Oberon Prime Set | 55p |
| Banshee Prime Set | 55p |
| Nezha Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
