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
**Last Updated:** 2026-01-20 23:11 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 300p |
| Braton Vandal Set | 250p |
| Dual Kamas Prime Set | 122p |
| Vauban Prime Set | 120p |
| Arum Spinosa Set | 110p |
| Akstiletto Prime Set | 100p |
| Hespar Set | 90p |
| Spira Prime Set | 81p |
| Tekko Prime Set | 76p |
| Nami Skyla Prime Set | 75p |
| Sporothrix Set | 72p |
| Latron Prime Set | 70p |
| Boar Prime Set | 70p |
| Dethcube Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Limbo Prime Set | 70p |
| Nyx Prime Set | 70p |
| Nekros Prime Set | 70p |
| Wukong Prime Set | 67p |
| Mirage Prime Set | 66p |
| Afuris Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Akbolto Prime Set | 65p |
| Corinth Prime Set | 65p |
| Khora Prime Set | 65p |
| Kronen Prime Set | 63p |
| Saryn Prime Set | 62p |
| Frost Prime Set | 61p |
| Rhino Prime Set | 61p |
| Valkyr Prime Set | 61p |
| Garuda Prime Set | 61p |
| Bo Prime Set | 60p |
| Carrier Prime Set | 60p |
| Atlas Prime Set | 60p |
| Loki Prime Set | 60p |
| Nova Prime Set | 60p |
| Octavia Prime Set | 60p |
| Nidus Prime Set | 60p |
| Titania Prime Set | 58p |
| Vectis Prime Set | 57p |
| Baza Prime Set | 57p |
| Xiphos Set | 57p |
| Chroma Prime Set | 57p |
| Oberon Prime Set | 56p |
| Nezha Prime Set | 56p |
| Morgha Set | 56p |
| Gara Prime Set | 56p |
| Kogake Prime Set | 55p |
| Trinity Prime Set | 55p |
| Ballistica Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)