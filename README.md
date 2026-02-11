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
**Last Updated:** 2026-02-11 12:57 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 265p |
| Braton Vandal Set | 265p |
| Vauban Prime Set | 123p |
| Dual Kamas Prime Set | 106p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 100p |
| Sporothrix Set | 99p |
| Limbo Prime Set | 76p |
| Nyx Prime Set | 75p |
| Akjagara Prime Set | 72p |
| Hespar Set | 72p |
| Wukong Prime Set | 70p |
| Dethcube Prime Set | 70p |
| Chroma Prime Set | 70p |
| Carmine Penta Set | 70p |
| Titania Prime Set | 67p |
| Kronen Prime Set | 67p |
| Nova Prime Set | 67p |
| Hydroid Prime Set | 66p |
| Rhino Prime Set | 66p |
| Nidus Prime Set | 66p |
| Nami Skyla Prime Set | 65p |
| Mirage Prime Set | 65p |
| Nekros Prime Set | 65p |
| Afuris Prime Set | 65p |
| Vectis Prime Set | 61p |
| Oberon Prime Set | 61p |
| Boar Prime Set | 61p |
| Kogake Prime Set | 61p |
| Carrier Prime Set | 61p |
| Atlas Prime Set | 61p |
| Bo Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Tekko Prime Set | 60p |
| Banshee Prime Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Gara Prime Set | 60p |
| Khora Prime Set | 60p |
| Aksomati Prime Set | 58p |
| Octavia Prime Set | 58p |
| Frost Prime Set | 56p |
| Mag Prime Set | 56p |
| Ballistica Prime Set | 56p |
| Valkyr Prime Set | 56p |
| Garuda Prime Set | 56p |
| Saryn Prime Set | 55p |
| Akbolto Prime Set | 55p |
| Xiphos Set | 55p |
| Spira Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
