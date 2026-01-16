# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
**Last Updated:** 2026-01-16 23:10 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 310p |
| Braton Vandal Set | 300p |
| Akstiletto Prime Set | 120p |
| Vauban Prime Set | 116p |
| Arum Spinosa Set | 110p |
| Dual Kamas Prime Set | 90p |
| Sporothrix Set | 90p |
| Limbo Prime Set | 80p |
| Tekko Prime Set | 80p |
| Dethcube Prime Set | 78p |
| Afuris Prime Set | 78p |
| Akjagara Prime Set | 76p |
| Nami Skyla Prime Set | 75p |
| Nekros Prime Set | 73p |
| Nyx Prime Set | 72p |
| Aksomati Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Wukong Prime Set | 70p |
| Spira Prime Set | 70p |
| Mirage Prime Set | 69p |
| Saryn Prime Set | 65p |
| Boar Prime Set | 65p |
| Akbolto Prime Set | 65p |
| Atlas Prime Set | 65p |
| Octavia Prime Set | 65p |
| Carmine Penta Set | 65p |
| Scourge Prime Set | 65p |
| Vectis Prime Set | 63p |
| Khora Prime Set | 63p |
| Frost Prime Set | 62p |
| Loki Prime Set | 62p |
| Hespar Set | 62p |
| Valkyr Prime Set | 61p |
| Kronen Prime Set | 61p |
| Garuda Prime Set | 61p |
| Rhino Prime Set | 60p |
| Carrier Prime Set | 60p |
| Titania Prime Set | 60p |
| Nova Prime Set | 60p |
| Corinth Prime Set | 60p |
| Nidus Prime Set | 60p |
| Ballistica Prime Set | 59p |
| Oberon Prime Set | 58p |
| Gara Prime Set | 56p |
| Wyrm Prime Set | 55p |
| Inaros Prime Set | 55p |
| Chroma Prime Set | 53p |
| Baza Prime Set | 52p |
| Sybaris Prime Set | 52p |
| Bo Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)