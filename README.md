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
**Last Updated:** 2026-03-17 17:00 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 215p |
| Lato Vandal Set | 200p |
| Dual Kamas Prime Set | 105p |
| Hespar Set | 101p |
| Kronen Prime Set | 85p |
| Afuris Prime Set | 85p |
| Wukong Prime Set | 80p |
| Limbo Prime Set | 80p |
| Arum Spinosa Set | 80p |
| Chroma Prime Set | 76p |
| Vauban Prime Set | 76p |
| Carrier Prime Set | 75p |
| Titania Prime Set | 75p |
| Nekros Prime Set | 75p |
| Corinth Prime Set | 75p |
| Hydroid Prime Set | 74p |
| Rhino Prime Set | 73p |
| Nami Skyla Prime Set | 72p |
| Nyx Prime Set | 72p |
| Akstiletto Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Spira Prime Set | 70p |
| Sporothrix Set | 70p |
| Mirage Prime Set | 70p |
| Gara Prime Set | 70p |
| Nidus Prime Set | 70p |
| Boar Prime Set | 68p |
| Latron Prime Set | 65p |
| Vectis Prime Set | 65p |
| Tipedo Prime Set | 65p |
| Octavia Prime Set | 65p |
| Khora Prime Set | 65p |
| Bo Prime Set | 62p |
| Banshee Prime Set | 62p |
| Zephyr Prime Set | 62p |
| Saryn Prime Set | 61p |
| Frost Prime Set | 60p |
| Oberon Prime Set | 60p |
| Kogake Prime Set | 60p |
| Ankyros Prime Set | 60p |
| Loki Prime Set | 60p |
| Equinox Prime Set | 60p |
| Carmine Penta Set | 60p |
| Hildryn Prime Set | 60p |
| Akarius Prime Set | 60p |
| Phantasma Prime Set | 59p |
| Akjagara Prime Set | 58p |
| Trinity Prime Set | 57p |
| Valkyr Prime Set | 56p |
| Tekko Prime Set | 56p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
