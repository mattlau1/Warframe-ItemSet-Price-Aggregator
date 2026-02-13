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
**Last Updated:** 2026-02-13 12:45 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 260p |
| Lato Vandal Set | 250p |
| Vauban Prime Set | 131p |
| Dual Kamas Prime Set | 100p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 100p |
| Hespar Set | 100p |
| Sporothrix Set | 99p |
| Xiphos Set | 90p |
| Limbo Prime Set | 81p |
| Spira Prime Set | 75p |
| Afuris Prime Set | 75p |
| Titania Prime Set | 67p |
| Chroma Prime Set | 67p |
| Corinth Prime Set | 66p |
| Vectis Prime Set | 65p |
| Wukong Prime Set | 65p |
| Boar Prime Set | 65p |
| Aksomati Prime Set | 65p |
| Nami Skyla Prime Set | 65p |
| Kronen Prime Set | 65p |
| Nova Prime Set | 65p |
| Nekros Prime Set | 65p |
| Nyx Prime Set | 63p |
| Loki Prime Set | 62p |
| Octavia Prime Set | 62p |
| Hydroid Prime Set | 61p |
| Tekko Prime Set | 61p |
| Nidus Prime Set | 61p |
| Latron Prime Set | 60p |
| Rhino Prime Set | 60p |
| Bo Prime Set | 60p |
| Carrier Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Akjagara Prime Set | 60p |
| Mirage Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Oberon Prime Set | 59p |
| Frost Prime Set | 56p |
| Wyrm Prime Set | 56p |
| Banshee Prime Set | 56p |
| Mag Prime Set | 55p |
| Tipedo Prime Set | 55p |
| Bonewidow Set | 54p |
| Scourge Prime Set | 53p |
| Trinity Prime Set | 52p |
| Valkyr Prime Set | 52p |
| Saryn Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
