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
**Last Updated:** 2026-03-21 20:20 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 216p |
| Braton Vandal Set | 180p |
| Hespar Set | 101p |
| Kronen Prime Set | 90p |
| Afuris Prime Set | 80p |
| Vauban Prime Set | 75p |
| Mirage Prime Set | 75p |
| Corinth Prime Set | 75p |
| Nami Skyla Prime Set | 71p |
| Nekros Prime Set | 71p |
| Wukong Prime Set | 70p |
| Titania Prime Set | 70p |
| Akstiletto Prime Set | 70p |
| Limbo Prime Set | 70p |
| Rhino Prime Set | 66p |
| Arum Spinosa Set | 66p |
| Hydroid Prime Set | 65p |
| Xiphos Set | 65p |
| Sporothrix Set | 65p |
| Gara Prime Set | 65p |
| Khora Prime Set | 65p |
| Latron Prime Set | 62p |
| Loki Prime Set | 62p |
| Saryn Prime Set | 61p |
| Zephyr Prime Set | 61p |
| Octavia Prime Set | 61p |
| Nidus Prime Set | 61p |
| Frost Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Carrier Prime Set | 60p |
| Chroma Prime Set | 60p |
| Nyx Prime Set | 60p |
| Carmine Penta Set | 60p |
| Prisma Shade Set | 60p |
| Wisp Prime Set | 60p |
| Aksomati Prime Set | 58p |
| Garuda Prime Set | 56p |
| Akvasto Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Nova Prime Set | 55p |
| Strun Prime Set | 55p |
| Cortege Set | 53p |
| Nautilus Set | 52p |
| Cinta Set | 52p |
| Spira Prime Set | 51p |
| Banshee Prime Set | 51p |
| Scourge Prime Set | 51p |
| Phantasma Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
