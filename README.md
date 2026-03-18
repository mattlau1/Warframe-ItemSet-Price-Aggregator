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
**Last Updated:** 2026-03-18 08:41 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 210p |
| Lato Vandal Set | 200p |
| Dual Kamas Prime Set | 100p |
| Hespar Set | 95p |
| Kronen Prime Set | 92p |
| Limbo Prime Set | 85p |
| Vauban Prime Set | 80p |
| Nyx Prime Set | 80p |
| Wukong Prime Set | 76p |
| Chroma Prime Set | 76p |
| Afuris Prime Set | 76p |
| Titania Prime Set | 75p |
| Mirage Prime Set | 75p |
| Gara Prime Set | 75p |
| Hydroid Prime Set | 74p |
| Akstiletto Prime Set | 72p |
| Nidus Prime Set | 72p |
| Rhino Prime Set | 71p |
| Corinth Prime Set | 71p |
| Carrier Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Arum Spinosa Set | 70p |
| Sporothrix Set | 70p |
| Nekros Prime Set | 70p |
| Carmine Penta Set | 68p |
| Oberon Prime Set | 66p |
| Boar Prime Set | 66p |
| Frost Prime Set | 65p |
| Vectis Prime Set | 65p |
| Xiphos Set | 65p |
| Zephyr Prime Set | 65p |
| Khora Prime Set | 65p |
| Bo Prime Set | 64p |
| Octavia Prime Set | 63p |
| Banshee Prime Set | 62p |
| Akarius Prime Set | 62p |
| Latron Prime Set | 61p |
| Mag Prime Set | 60p |
| Panthera Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Spira Prime Set | 60p |
| Nami Skyla Prime Set | 60p |
| Loki Prime Set | 60p |
| Nova Prime Set | 60p |
| Equinox Prime Set | 60p |
| Strun Prime Set | 60p |
| Aeolak Set | 60p |
| Wisp Prime Set | 60p |
| Trinity Prime Set | 57p |
| Valkyr Prime Set | 56p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
