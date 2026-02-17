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
**Last Updated:** 2026-02-17 08:38 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 250p |
| Lato Vandal Set | 220p |
| Vauban Prime Set | 100p |
| Dual Kamas Prime Set | 95p |
| Arum Spinosa Set | 90p |
| Hespar Set | 90p |
| Sporothrix Set | 81p |
| Nami Skyla Prime Set | 75p |
| Vectis Prime Set | 70p |
| Limbo Prime Set | 70p |
| Wukong Prime Set | 65p |
| Chroma Prime Set | 65p |
| Nyx Prime Set | 65p |
| Xiphos Set | 62p |
| Kronen Prime Set | 62p |
| Nova Prime Set | 62p |
| Rhino Prime Set | 61p |
| Hydroid Prime Set | 60p |
| Titania Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Mirage Prime Set | 60p |
| Nekros Prime Set | 60p |
| Octavia Prime Set | 60p |
| Carmine Penta Set | 60p |
| Ankyros Prime Set | 57p |
| Boar Prime Set | 56p |
| Gara Prime Set | 56p |
| Frost Prime Set | 55p |
| Mag Prime Set | 55p |
| Bo Prime Set | 55p |
| Boltor Prime Set | 55p |
| Spira Prime Set | 55p |
| Loki Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Wyrm Prime Set | 53p |
| Afuris Prime Set | 53p |
| Aksomati Prime Set | 52p |
| Saryn Prime Set | 50p |
| Helios Prime Set | 50p |
| Kogake Prime Set | 50p |
| Ballistica Prime Set | 50p |
| Carrier Prime Set | 50p |
| Dethcube Prime Set | 50p |
| Akstiletto Prime Set | 50p |
| Nidus Prime Set | 50p |
| Khora Prime Set | 50p |
| Phantasma Prime Set | 50p |
| Oberon Prime Set | 49p |
| Valkyr Prime Set | 47p |
| Atlas Prime Set | 46p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
