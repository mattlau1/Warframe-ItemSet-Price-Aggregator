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
**Last Updated:** 2026-02-19 08:37 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 280p |
| Lato Vandal Set | 260p |
| Vauban Prime Set | 140p |
| Akstiletto Prime Set | 101p |
| Dual Kamas Prime Set | 100p |
| Arum Spinosa Set | 90p |
| Nami Skyla Prime Set | 85p |
| Sporothrix Set | 81p |
| Hespar Set | 81p |
| Aksomati Prime Set | 75p |
| Spira Prime Set | 75p |
| Kronen Prime Set | 75p |
| Limbo Prime Set | 72p |
| Nova Prime Set | 71p |
| Titania Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nyx Prime Set | 70p |
| Hydroid Prime Set | 66p |
| Wukong Prime Set | 65p |
| Oberon Prime Set | 65p |
| Xiphos Set | 65p |
| Tekko Prime Set | 65p |
| Corinth Prime Set | 65p |
| Nidus Prime Set | 65p |
| Afuris Prime Set | 65p |
| Nekros Prime Set | 62p |
| Vectis Prime Set | 61p |
| Ballistica Prime Set | 60p |
| Carrier Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Banshee Prime Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Mirage Prime Set | 60p |
| Gara Prime Set | 60p |
| Khora Prime Set | 60p |
| Rhino Prime Set | 55p |
| Mag Prime Set | 55p |
| Bo Prime Set | 55p |
| Kogake Prime Set | 55p |
| Atlas Prime Set | 55p |
| Octavia Prime Set | 55p |
| Akarius Prime Set | 52p |
| Frost Prime Set | 51p |
| Dethcube Prime Set | 51p |
| Valkyr Prime Set | 51p |
| Phantasma Prime Set | 51p |
| Saryn Prime Set | 50p |
| Trinity Prime Set | 50p |
| Latron Wraith Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
