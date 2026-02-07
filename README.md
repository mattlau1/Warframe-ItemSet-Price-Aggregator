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
**Last Updated:** 2026-02-07 12:36 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 285p |
| Braton Vandal Set | 276p |
| Vauban Prime Set | 131p |
| Dual Kamas Prime Set | 115p |
| Akstiletto Prime Set | 110p |
| Arum Spinosa Set | 100p |
| Hespar Set | 100p |
| Sporothrix Set | 90p |
| Xiphos Set | 87p |
| Limbo Prime Set | 80p |
| Akbolto Prime Set | 76p |
| Afuris Prime Set | 75p |
| Nyx Prime Set | 72p |
| Wukong Prime Set | 71p |
| Chroma Prime Set | 71p |
| Akjagara Prime Set | 71p |
| Spira Prime Set | 70p |
| Tekko Prime Set | 70p |
| Nova Prime Set | 70p |
| Titania Prime Set | 68p |
| Nekros Prime Set | 67p |
| Hydroid Prime Set | 65p |
| Bo Prime Set | 65p |
| Boar Prime Set | 65p |
| Dethcube Prime Set | 65p |
| Mirage Prime Set | 65p |
| Gara Prime Set | 65p |
| Kronen Prime Set | 64p |
| Oberon Prime Set | 63p |
| Nami Skyla Prime Set | 63p |
| Aksomati Prime Set | 62p |
| Nidus Prime Set | 62p |
| Vectis Prime Set | 61p |
| Boltor Prime Set | 61p |
| Atlas Prime Set | 61p |
| Octavia Prime Set | 61p |
| Rhino Prime Set | 60p |
| Khora Prime Set | 60p |
| Latron Prime Set | 56p |
| Mag Prime Set | 56p |
| Kogake Prime Set | 56p |
| Loki Prime Set | 56p |
| Carmine Penta Set | 56p |
| Carrier Prime Set | 55p |
| Wyrm Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Banshee Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Scourge Prime Set | 55p |
| Akarius Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
