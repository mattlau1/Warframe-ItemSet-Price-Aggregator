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
**Last Updated:** 2026-02-27 20:22 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 260p |
| Braton Vandal Set | 200p |
| Dual Kamas Prime Set | 125p |
| Akstiletto Prime Set | 88p |
| Carmine Penta Set | 85p |
| Vauban Prime Set | 82p |
| Kronen Prime Set | 81p |
| Hespar Set | 81p |
| Spira Prime Set | 80p |
| Cortege Set | 80p |
| Morgha Set | 80p |
| Limbo Prime Set | 75p |
| Nyx Prime Set | 75p |
| Wukong Prime Set | 72p |
| Corinth Prime Set | 72p |
| Sporothrix Set | 71p |
| Mirage Prime Set | 71p |
| Vectis Prime Set | 70p |
| Titania Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nekros Prime Set | 67p |
| Nova Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Octavia Prime Set | 65p |
| Rhino Prime Set | 62p |
| Carrier Prime Set | 62p |
| Trinity Prime Set | 61p |
| Banshee Prime Set | 61p |
| Frost Prime Set | 60p |
| Oberon Prime Set | 60p |
| Boltor Prime Set | 60p |
| Arum Spinosa Set | 60p |
| Loki Prime Set | 60p |
| Gara Prime Set | 60p |
| Nidus Prime Set | 60p |
| Khora Prime Set | 60p |
| Afuris Prime Set | 60p |
| Boar Prime Set | 59p |
| Akjagara Prime Set | 58p |
| Saryn Prime Set | 57p |
| Valkyr Prime Set | 56p |
| Garuda Prime Set | 56p |
| Latron Prime Set | 55p |
| Ballistica Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Nezha Prime Set | 55p |
| Phantasma Prime Set | 55p |
| Wisp Prime Set | 55p |
| Wyrm Prime Set | 53p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
