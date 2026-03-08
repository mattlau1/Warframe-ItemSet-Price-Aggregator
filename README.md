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
**Last Updated:** 2026-03-08 08:25 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 221p |
| Braton Vandal Set | 212p |
| Xiphos Set | 105p |
| Hespar Set | 100p |
| Dual Kamas Prime Set | 91p |
| Sporothrix Set | 85p |
| Limbo Prime Set | 80p |
| Kronen Prime Set | 80p |
| Wukong Prime Set | 76p |
| Nyx Prime Set | 76p |
| Kogake Prime Set | 75p |
| Akstiletto Prime Set | 75p |
| Arum Spinosa Set | 75p |
| Vauban Prime Set | 75p |
| Mirage Prime Set | 75p |
| Nami Skyla Prime Set | 72p |
| Chroma Prime Set | 72p |
| Titania Prime Set | 71p |
| Corinth Prime Set | 71p |
| Octavia Prime Set | 70p |
| Nidus Prime Set | 70p |
| Nekros Prime Set | 68p |
| Hydroid Prime Set | 66p |
| Rhino Prime Set | 66p |
| Nova Prime Set | 65p |
| Gara Prime Set | 63p |
| Boar Prime Set | 62p |
| Loki Prime Set | 61p |
| Carmine Penta Set | 61p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Carrier Prime Set | 60p |
| Banshee Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Khora Prime Set | 60p |
| Akarius Prime Set | 60p |
| Frost Prime Set | 58p |
| Saryn Prime Set | 58p |
| Akbolto Prime Set | 58p |
| Akjagara Prime Set | 58p |
| Baruuk Prime Set | 57p |
| Trinity Prime Set | 56p |
| Valkyr Prime Set | 56p |
| Vectis Prime Set | 55p |
| Bo Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Bonewidow Set | 55p |
| Equinox Prime Set | 55p |
| Nezha Prime Set | 55p |
| Phantasma Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
