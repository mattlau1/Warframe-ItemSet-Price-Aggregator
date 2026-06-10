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
**Last Updated:** 2026-06-10 21:54 UTC

| Item Set | Median Price |
| :--- | :--- |
| Xiphos Set | 105p |
| Vectis Prime Set | 100p |
| Vauban Prime Set | 91p |
| Akbolto Prime Set | 90p |
| Kronen Prime Set | 90p |
| Limbo Prime Set | 88p |
| Nekros Prime Set | 83p |
| Hydroid Prime Set | 80p |
| Hespar Set | 80p |
| Titania Prime Set | 75p |
| Chroma Prime Set | 75p |
| Mirage Prime Set | 75p |
| Nidus Prime Set | 75p |
| Garuda Prime Set | 75p |
| Scourge Prime Set | 72p |
| Frost Prime Set | 71p |
| Saryn Prime Set | 70p |
| Oberon Prime Set | 70p |
| Spira Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Akjagara Prime Set | 70p |
| Corinth Prime Set | 70p |
| Octavia Prime Set | 70p |
| Khora Prime Set | 70p |
| Banshee Prime Set | 66p |
| Gara Prime Set | 66p |
| Wukong Prime Set | 65p |
| Loki Prime Set | 65p |
| Baza Prime Set | 64p |
| Mag Prime Set | 62p |
| Dual Kamas Prime Set | 61p |
| Aksomati Prime Set | 61p |
| Valkyr Prime Set | 61p |
| Zephyr Prime Set | 61p |
| Nautilus Set | 61p |
| Helios Prime Set | 60p |
| Latron Prime Set | 60p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Glaive Prime Set | 60p |
| Nova Prime Set | 60p |
| Wisp Prime Set | 60p |
| Hildryn Prime Set | 59p |
| Baruuk Prime Set | 56p |
| Mesa Prime Set | 55p |
| Aeolak Set | 55p |
| Phantasma Prime Set | 55p |
| Revenant Prime Set | 53p |
| Carrier Prime Set | 52p |
| Akstiletto Prime Set | 52p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
