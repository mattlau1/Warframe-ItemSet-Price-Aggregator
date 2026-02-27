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
**Last Updated:** 2026-02-27 08:35 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 275p |
| Lato Vandal Set | 265p |
| Dual Kamas Prime Set | 110p |
| Hespar Set | 93p |
| Vauban Prime Set | 90p |
| Akstiletto Prime Set | 85p |
| Kronen Prime Set | 80p |
| Wukong Prime Set | 75p |
| Titania Prime Set | 75p |
| Nyx Prime Set | 75p |
| Mirage Prime Set | 72p |
| Rhino Prime Set | 70p |
| Limbo Prime Set | 70p |
| Spira Prime Set | 70p |
| Sporothrix Set | 70p |
| Chroma Prime Set | 70p |
| Nova Prime Set | 70p |
| Octavia Prime Set | 70p |
| Hydroid Prime Set | 65p |
| Tekko Prime Set | 65p |
| Nekros Prime Set | 65p |
| Carmine Penta Set | 65p |
| Gara Prime Set | 65p |
| Vectis Prime Set | 61p |
| Ankyros Prime Set | 61p |
| Nidus Prime Set | 61p |
| Frost Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Corinth Prime Set | 60p |
| Khora Prime Set | 60p |
| Baruuk Prime Set | 60p |
| Helios Prime Set | 59p |
| Saryn Prime Set | 57p |
| Trinity Prime Set | 57p |
| Mag Prime Set | 55p |
| Oberon Prime Set | 55p |
| Boar Prime Set | 55p |
| Inaros Prime Set | 55p |
| Arum Spinosa Set | 55p |
| Cortege Set | 55p |
| Banshee Prime Set | 55p |
| Afuris Prime Set | 55p |
| Wisp Prime Set | 54p |
| Wyrm Prime Set | 53p |
| Hildryn Prime Set | 52p |
| Destreza Prime Set | 51p |
| Carrier Prime Set | 51p |
| Atlas Prime Set | 51p |
| Akjagara Prime Set | 51p |
| Bo Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
