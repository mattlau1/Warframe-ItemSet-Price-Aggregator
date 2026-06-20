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
**Last Updated:** 2026-06-20 02:48 UTC

| Item Set | Median Price |
| :--- | :--- |
| Styanax Prime Set | 120p |
| Afentis Prime Set | 100p |
| Vauban Prime Set | 95p |
| Vectis Prime Set | 90p |
| Spira Prime Set | 90p |
| Nidus Prime Set | 85p |
| Hespar Set | 85p |
| Limbo Prime Set | 82p |
| Ballistica Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Kronen Prime Set | 80p |
| Nekros Prime Set | 80p |
| Athodai Prime Set | 76p |
| Hydroid Prime Set | 75p |
| Scourge Prime Set | 72p |
| Frost Prime Set | 71p |
| Carrier Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Titania Prime Set | 70p |
| Banshee Prime Set | 70p |
| Loki Prime Set | 70p |
| Garuda Prime Set | 70p |
| Khora Prime Set | 70p |
| Afuris Prime Set | 70p |
| Octavia Prime Set | 67p |
| Akbolto Prime Set | 65p |
| Gara Prime Set | 65p |
| Phantasma Prime Set | 65p |
| Wukong Prime Set | 62p |
| Saryn Prime Set | 61p |
| Akstiletto Prime Set | 61p |
| Chroma Prime Set | 61p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Boar Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Nova Prime Set | 60p |
| Akjagara Prime Set | 60p |
| Mirage Prime Set | 60p |
| Corinth Prime Set | 60p |
| Nautilus Set | 60p |
| Carmine Penta Set | 60p |
| Baza Prime Set | 58p |
| Wisp Prime Set | 56p |
| Destreza Prime Set | 55p |
| Ember Prime Set | 55p |
| Glaive Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Zephyr Prime Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
