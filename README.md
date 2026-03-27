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
**Last Updated:** 2026-03-27 08:44 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 93p |
| Afuris Prime Set | 76p |
| Kronen Prime Set | 75p |
| Chroma Prime Set | 75p |
| Vauban Prime Set | 75p |
| Mirage Prime Set | 75p |
| Limbo Prime Set | 72p |
| Nami Skyla Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Carrier Prime Set | 70p |
| Nekros Prime Set | 70p |
| Gara Prime Set | 70p |
| Titania Prime Set | 66p |
| Rhino Prime Set | 65p |
| Boar Prime Set | 65p |
| Akstiletto Prime Set | 65p |
| Spira Prime Set | 65p |
| Ivara Prime Set | 65p |
| Nidus Prime Set | 65p |
| Wukong Prime Set | 62p |
| Oberon Prime Set | 61p |
| Octavia Prime Set | 61p |
| Khora Prime Set | 61p |
| Dual Kamas Prime Set | 60p |
| Mag Prime Set | 60p |
| Kogake Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Nyx Prime Set | 60p |
| Carmine Penta Set | 60p |
| Aksomati Prime Set | 57p |
| Saryn Prime Set | 55p |
| Boltor Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Cortege Set | 55p |
| Banshee Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Strun Prime Set | 55p |
| Scourge Prime Set | 53p |
| Hildryn Prime Set | 52p |
| Cinta Set | 52p |
| Vectis Prime Set | 51p |
| Garuda Prime Set | 51p |
| Frost Prime Set | 50p |
| Bo Prime Set | 50p |
| Ankyros Prime Set | 50p |
| Amesha Set | 50p |
| Karak Wraith Set | 50p |
| Wyrm Prime Set | 50p |
| Glaive Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
