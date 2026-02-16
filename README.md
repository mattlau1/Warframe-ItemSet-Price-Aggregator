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
**Last Updated:** 2026-02-16 05:25 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 250p |
| Braton Vandal Set | 250p |
| Vauban Prime Set | 130p |
| Dual Kamas Prime Set | 90p |
| Hespar Set | 86p |
| Arum Spinosa Set | 80p |
| Limbo Prime Set | 75p |
| Nami Skyla Prime Set | 75p |
| Vectis Prime Set | 70p |
| Carrier Prime Set | 70p |
| Akstiletto Prime Set | 70p |
| Chroma Prime Set | 66p |
| Wukong Prime Set | 65p |
| Titania Prime Set | 65p |
| Akbolto Prime Set | 65p |
| Sporothrix Set | 65p |
| Nova Prime Set | 65p |
| Nyx Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Nekros Prime Set | 65p |
| Kronen Prime Set | 62p |
| Frost Prime Set | 60p |
| Mag Prime Set | 60p |
| Xiphos Set | 60p |
| Spira Prime Set | 60p |
| Bonewidow Set | 60p |
| Mirage Prime Set | 60p |
| Octavia Prime Set | 60p |
| Nidus Prime Set | 60p |
| Gara Prime Set | 59p |
| Rhino Prime Set | 58p |
| Afuris Prime Set | 58p |
| Boar Prime Set | 56p |
| Trinity Prime Set | 56p |
| Aksomati Prime Set | 55p |
| Loki Prime Set | 55p |
| Wyrm Prime Set | 53p |
| Valkyr Prime Set | 52p |
| Saryn Prime Set | 51p |
| Hydroid Prime Set | 50p |
| Oberon Prime Set | 50p |
| Bo Prime Set | 50p |
| Dethcube Prime Set | 50p |
| Baza Prime Set | 50p |
| Atlas Prime Set | 50p |
| Tekko Prime Set | 50p |
| Khora Prime Set | 50p |
| Akarius Prime Set | 50p |
| Hildryn Prime Set | 48p |
| Wisp Prime Set | 48p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
