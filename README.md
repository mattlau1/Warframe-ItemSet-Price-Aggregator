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
**Last Updated:** 2026-03-29 08:34 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 101p |
| Akbolto Prime Set | 90p |
| Vectis Prime Set | 80p |
| Wukong Prime Set | 75p |
| Titania Prime Set | 75p |
| Limbo Prime Set | 75p |
| Vauban Prime Set | 75p |
| Mirage Prime Set | 75p |
| Nekros Prime Set | 75p |
| Chroma Prime Set | 73p |
| Akstiletto Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Dual Kamas Prime Set | 70p |
| Rhino Prime Set | 70p |
| Braton Vandal Set | 70p |
| Carrier Prime Set | 70p |
| Spira Prime Set | 70p |
| Nami Skyla Prime Set | 68p |
| Xiphos Set | 67p |
| Boar Prime Set | 65p |
| Nyx Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Nidus Prime Set | 65p |
| Banshee Prime Set | 62p |
| Oberon Prime Set | 61p |
| Kronen Prime Set | 61p |
| Octavia Prime Set | 61p |
| Destreza Prime Set | 60p |
| Bo Prime Set | 60p |
| Lato Vandal Set | 60p |
| Ballistica Prime Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Corinth Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Khora Prime Set | 60p |
| Afuris Prime Set | 60p |
| Frost Prime Set | 55p |
| Boltor Prime Set | 55p |
| Kogake Prime Set | 55p |
| Aksomati Prime Set | 55p |
| Cortege Set | 55p |
| Equinox Prime Set | 55p |
| Nezha Prime Set | 55p |
| Tenora Prime Set | 55p |
| Scourge Prime Set | 55p |
| Garuda Prime Set | 55p |
| Cinta Set | 55p |
| Inaros Prime Set | 54p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
