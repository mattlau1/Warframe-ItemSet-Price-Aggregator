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
**Last Updated:** 2026-03-14 01:28 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 241p |
| Braton Vandal Set | 210p |
| Hespar Set | 111p |
| Scimitar Set | 100p |
| Dual Kamas Prime Set | 95p |
| Afuris Prime Set | 95p |
| Limbo Prime Set | 85p |
| Akbolto Prime Set | 82p |
| Vauban Prime Set | 81p |
| Kronen Prime Set | 80p |
| Sporothrix Set | 80p |
| Titania Prime Set | 75p |
| Xiphos Set | 72p |
| Nyx Prime Set | 72p |
| Corinth Prime Set | 71p |
| Wukong Prime Set | 70p |
| Boar Prime Set | 70p |
| Carrier Prime Set | 70p |
| Spira Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Chroma Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nekros Prime Set | 70p |
| Gara Prime Set | 70p |
| Aksomati Prime Set | 69p |
| Akjagara Prime Set | 69p |
| Rhino Prime Set | 66p |
| Tipedo Prime Set | 66p |
| Khora Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Vectis Prime Set | 65p |
| Bo Prime Set | 65p |
| Kogake Prime Set | 65p |
| Arum Spinosa Set | 65p |
| Octavia Prime Set | 65p |
| Nidus Prime Set | 65p |
| Carmine Penta Set | 63p |
| Frost Prime Set | 62p |
| Phantasma Prime Set | 61p |
| Saryn Prime Set | 60p |
| Boltor Prime Set | 60p |
| Ankyros Prime Set | 60p |
| Akstiletto Prime Set | 60p |
| Panthera Prime Set | 60p |
| Nova Prime Set | 60p |
| Cinta Set | 60p |
| Akarius Prime Set | 60p |
| Ballistica Prime Set | 56p |
| Oberon Prime Set | 55p |
| Valkyr Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
