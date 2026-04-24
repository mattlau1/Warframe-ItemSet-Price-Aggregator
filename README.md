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
**Last Updated:** 2026-04-24 06:05 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 101p |
| Vectis Prime Set | 90p |
| Kronen Prime Set | 90p |
| Afuris Prime Set | 90p |
| Limbo Prime Set | 85p |
| Carmine Penta Set | 85p |
| Vauban Prime Set | 83p |
| Rhino Prime Set | 80p |
| Aksomati Prime Set | 80p |
| Hydroid Prime Set | 75p |
| Titania Prime Set | 75p |
| Spira Prime Set | 75p |
| Nyx Prime Set | 75p |
| Mirage Prime Set | 75p |
| Nekros Prime Set | 75p |
| Kogake Prime Set | 72p |
| Chroma Prime Set | 72p |
| Wukong Prime Set | 71p |
| Voruna Prime Set | 71p |
| Akstiletto Prime Set | 70p |
| Xiphos Set | 70p |
| Nami Skyla Prime Set | 66p |
| Morgha Set | 66p |
| Octavia Prime Set | 66p |
| Frost Prime Set | 65p |
| Ballistica Prime Set | 65p |
| Banshee Prime Set | 65p |
| Loki Prime Set | 65p |
| Zephyr Prime Set | 65p |
| Nidus Prime Set | 65p |
| Khora Prime Set | 65p |
| Cinta Set | 65p |
| Boar Prime Set | 63p |
| Cortege Set | 62p |
| Carrier Prime Set | 61p |
| Saryn Prime Set | 60p |
| Akvasto Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Bonewidow Set | 60p |
| Corinth Prime Set | 60p |
| Nautilus Set | 60p |
| Imperator Vandal Set | 57p |
| Nezha Prime Set | 57p |
| Bo Prime Set | 56p |
| Aeolak Set | 56p |
| Dual Kamas Prime Set | 55p |
| Latron Prime Set | 55p |
| Inaros Prime Set | 55p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
