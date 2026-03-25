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
**Last Updated:** 2026-03-25 16:57 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 140p |
| Hespar Set | 103p |
| Lato Vandal Set | 100p |
| Kronen Prime Set | 90p |
| Limbo Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Vauban Prime Set | 80p |
| Afuris Prime Set | 80p |
| Chroma Prime Set | 76p |
| Wukong Prime Set | 75p |
| Titania Prime Set | 75p |
| Akstiletto Prime Set | 75p |
| Mirage Prime Set | 72p |
| Nekros Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Dual Kamas Prime Set | 70p |
| Rhino Prime Set | 70p |
| Boar Prime Set | 70p |
| Arum Spinosa Set | 70p |
| Corinth Prime Set | 70p |
| Gara Prime Set | 70p |
| Nidus Prime Set | 69p |
| Octavia Prime Set | 66p |
| Carrier Prime Set | 65p |
| Khora Prime Set | 65p |
| Loki Prime Set | 62p |
| Zephyr Prime Set | 62p |
| Latron Prime Set | 61p |
| Oberon Prime Set | 61p |
| Frost Prime Set | 60p |
| Saryn Prime Set | 60p |
| Mag Prime Set | 60p |
| Bo Prime Set | 60p |
| Kogake Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Banshee Prime Set | 60p |
| Nova Prime Set | 60p |
| Nyx Prime Set | 60p |
| Equinox Prime Set | 59p |
| Garuda Prime Set | 57p |
| Nezha Prime Set | 56p |
| Glaive Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Baruuk Prime Set | 55p |
| Hildryn Prime Set | 55p |
| Wisp Prime Set | 55p |
| Scourge Prime Set | 53p |
| Inaros Prime Set | 52p |
| Vectis Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
