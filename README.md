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
**Last Updated:** 2026-04-07 05:44 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 100p |
| Vectis Prime Set | 85p |
| Kronen Prime Set | 80p |
| Afuris Prime Set | 80p |
| Limbo Prime Set | 76p |
| Wukong Prime Set | 75p |
| Aksomati Prime Set | 75p |
| Vauban Prime Set | 75p |
| Mirage Prime Set | 75p |
| Chroma Prime Set | 73p |
| Nekros Prime Set | 72p |
| Nyx Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Destreza Prime Set | 70p |
| Carrier Prime Set | 70p |
| Carmine Penta Set | 70p |
| Khora Prime Set | 68p |
| Rhino Prime Set | 66p |
| Gara Prime Set | 66p |
| Boar Prime Set | 65p |
| Titania Prime Set | 65p |
| Akstiletto Prime Set | 65p |
| Octavia Prime Set | 65p |
| Mag Prime Set | 61p |
| Nami Skyla Prime Set | 61p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Boltor Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Spira Prime Set | 60p |
| Loki Prime Set | 60p |
| Akjagara Prime Set | 60p |
| Zephyr Prime Set | 57p |
| Frost Prime Set | 56p |
| Dual Kamas Prime Set | 56p |
| Banshee Prime Set | 56p |
| Saryn Prime Set | 55p |
| Latron Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Equinox Prime Set | 55p |
| Mesa Prime Set | 55p |
| Phantasma Prime Set | 55p |
| Corinth Prime Set | 52p |
| Scourge Prime Set | 52p |
| Kogake Prime Set | 51p |
| Inaros Prime Set | 50p |
| Bonewidow Set | 50p |
| Cortege Set | 50p |
| Nova Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
