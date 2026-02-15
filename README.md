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
**Last Updated:** 2026-02-15 05:17 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 250p |
| Braton Vandal Set | 240p |
| Vauban Prime Set | 122p |
| Hespar Set | 100p |
| Dual Kamas Prime Set | 90p |
| Akstiletto Prime Set | 88p |
| Sporothrix Set | 82p |
| Kronen Prime Set | 81p |
| Limbo Prime Set | 80p |
| Xiphos Set | 80p |
| Spira Prime Set | 75p |
| Akjagara Prime Set | 75p |
| Nami Skyla Prime Set | 70p |
| Nyx Prime Set | 68p |
| Wukong Prime Set | 67p |
| Nova Prime Set | 66p |
| Nidus Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Rhino Prime Set | 65p |
| Aksomati Prime Set | 65p |
| Titania Prime Set | 65p |
| Chroma Prime Set | 65p |
| Mirage Prime Set | 65p |
| Nekros Prime Set | 61p |
| Frost Prime Set | 60p |
| Oberon Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Tekko Prime Set | 60p |
| Loki Prime Set | 60p |
| Afuris Prime Set | 60p |
| Alternox Prime Set | 60p |
| Octavia Prime Set | 58p |
| Dethcube Prime Set | 56p |
| Banshee Prime Set | 56p |
| Nautilus Set | 56p |
| Vectis Prime Set | 55p |
| Bo Prime Set | 55p |
| Boar Prime Set | 55p |
| Boltor Prime Set | 55p |
| Trinity Prime Set | 55p |
| Gara Prime Set | 55p |
| Wyrm Prime Set | 53p |
| Kogake Prime Set | 52p |
| Morgha Set | 52p |
| Helios Prime Set | 51p |
| Mag Prime Set | 51p |
| Ivara Prime Set | 51p |
| Baruuk Prime Set | 51p |
| Saryn Prime Set | 50p |
| Ballistica Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
