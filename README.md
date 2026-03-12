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
**Last Updated:** 2026-03-12 16:55 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 230p |
| Braton Vandal Set | 230p |
| Dual Kamas Prime Set | 115p |
| Hespar Set | 110p |
| Afuris Prime Set | 86p |
| Limbo Prime Set | 81p |
| Kogake Prime Set | 80p |
| Kronen Prime Set | 80p |
| Corinth Prime Set | 76p |
| Wukong Prime Set | 75p |
| Titania Prime Set | 75p |
| Vauban Prime Set | 75p |
| Nyx Prime Set | 75p |
| Chroma Prime Set | 73p |
| Akstiletto Prime Set | 72p |
| Vectis Prime Set | 71p |
| Carrier Prime Set | 71p |
| Akbolto Prime Set | 71p |
| Mirage Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Rhino Prime Set | 70p |
| Boar Prime Set | 70p |
| Xiphos Set | 70p |
| Spira Prime Set | 70p |
| Arum Spinosa Set | 70p |
| Sporothrix Set | 70p |
| Octavia Prime Set | 70p |
| Gara Prime Set | 70p |
| Nidus Prime Set | 70p |
| Nekros Prime Set | 68p |
| Nova Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Khora Prime Set | 65p |
| Frost Prime Set | 63p |
| Zephyr Prime Set | 61p |
| Phantasma Prime Set | 61p |
| Mag Prime Set | 60p |
| Bo Prime Set | 60p |
| Trinity Prime Set | 60p |
| Panthera Prime Set | 60p |
| Nami Skyla Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Loki Prime Set | 60p |
| Carmine Penta Set | 60p |
| Cinta Set | 60p |
| Oberon Prime Set | 59p |
| Saryn Prime Set | 58p |
| Banshee Prime Set | 57p |
| Ballistica Prime Set | 56p |
| Destreza Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
