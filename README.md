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
**Last Updated:** 2026-05-11 07:36 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 100p |
| Xiphos Set | 95p |
| Afuris Prime Set | 88p |
| Vauban Prime Set | 85p |
| Vectis Prime Set | 80p |
| Limbo Prime Set | 80p |
| Kronen Prime Set | 80p |
| Nekros Prime Set | 80p |
| Wukong Prime Set | 76p |
| Akbolto Prime Set | 76p |
| Chroma Prime Set | 75p |
| Mirage Prime Set | 75p |
| Nidus Prime Set | 75p |
| Boar Prime Set | 72p |
| Titania Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Akstiletto Prime Set | 69p |
| Akjagara Prime Set | 69p |
| Cortege Set | 67p |
| Garuda Prime Set | 67p |
| Bo Prime Set | 66p |
| Frost Prime Set | 65p |
| Saryn Prime Set | 65p |
| Latron Prime Set | 65p |
| Carrier Prime Set | 65p |
| Octavia Prime Set | 65p |
| Khora Prime Set | 65p |
| Oberon Prime Set | 63p |
| Banshee Prime Set | 61p |
| Kogake Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Spira Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Corinth Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Mag Prime Set | 57p |
| Loki Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Rhino Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Prisma Shade Set | 55p |
| Hildryn Prime Set | 55p |
| Wisp Prime Set | 55p |
| Akarius Prime Set | 55p |
| Voruna Prime Set | 55p |
| Dethcube Prime Set | 53p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
