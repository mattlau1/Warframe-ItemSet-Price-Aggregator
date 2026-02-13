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
**Last Updated:** 2026-02-13 05:19 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 260p |
| Lato Vandal Set | 255p |
| Vauban Prime Set | 126p |
| Hespar Set | 90p |
| Limbo Prime Set | 80p |
| Arum Spinosa Set | 80p |
| Dual Kamas Prime Set | 75p |
| Akbolto Prime Set | 75p |
| Xiphos Set | 75p |
| Spira Prime Set | 70p |
| Chroma Prime Set | 70p |
| Hydroid Prime Set | 65p |
| Wukong Prime Set | 65p |
| Aksomati Prime Set | 65p |
| Titania Prime Set | 65p |
| Nova Prime Set | 65p |
| Mirage Prime Set | 65p |
| Corinth Prime Set | 65p |
| Nyx Prime Set | 62p |
| Nekros Prime Set | 62p |
| Carrier Prime Set | 61p |
| Nidus Prime Set | 61p |
| Vectis Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Nami Skyla Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Banshee Prime Set | 56p |
| Frost Prime Set | 55p |
| Latron Prime Set | 55p |
| Mag Prime Set | 55p |
| Kronen Prime Set | 55p |
| Atlas Prime Set | 55p |
| Sporothrix Set | 55p |
| Loki Prime Set | 55p |
| Akstiletto Prime Set | 53p |
| Octavia Prime Set | 53p |
| Dethcube Prime Set | 52p |
| Akjagara Prime Set | 51p |
| Saryn Prime Set | 50p |
| Rhino Prime Set | 50p |
| Trinity Prime Set | 50p |
| Valkyr Prime Set | 50p |
| Tekko Prime Set | 50p |
| Nezha Prime Set | 50p |
| Garuda Prime Set | 50p |
| Khora Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
