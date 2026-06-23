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
**Last Updated:** 2026-06-23 02:42 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 131p |
| Xiphos Set | 102p |
| Destreza Prime Set | 100p |
| Vectis Prime Set | 100p |
| Styanax Prime Set | 95p |
| Nidus Prime Set | 90p |
| Vauban Prime Set | 86p |
| Hespar Set | 85p |
| Limbo Prime Set | 80p |
| Spira Prime Set | 80p |
| Nekros Prime Set | 80p |
| Afuris Prime Set | 80p |
| Afentis Prime Set | 80p |
| Garuda Prime Set | 76p |
| Hydroid Prime Set | 75p |
| Kronen Prime Set | 75p |
| Akjagara Prime Set | 75p |
| Mirage Prime Set | 71p |
| Akstiletto Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Loki Prime Set | 70p |
| Octavia Prime Set | 70p |
| Scourge Prime Set | 70p |
| Frost Prime Set | 68p |
| Saryn Prime Set | 65p |
| Carrier Prime Set | 65p |
| Titania Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Nami Skyla Prime Set | 65p |
| Zephyr Prime Set | 65p |
| Corinth Prime Set | 65p |
| Gara Prime Set | 65p |
| Aksomati Prime Set | 62p |
| Wukong Prime Set | 60p |
| Oberon Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Carmine Penta Set | 60p |
| Khora Prime Set | 60p |
| Cinta Set | 60p |
| Panthera Prime Set | 56p |
| Nezha Prime Set | 56p |
| Phantasma Prime Set | 56p |
| Wisp Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Mag Prime Set | 55p |
| Bo Prime Set | 55p |
| Boar Prime Set | 55p |
| Baza Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Volt Prime Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
