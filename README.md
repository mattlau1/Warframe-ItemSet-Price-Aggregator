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
**Last Updated:** 2026-02-21 12:35 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 275p |
| Lato Vandal Set | 250p |
| Arum Spinosa Set | 110p |
| Akstiletto Prime Set | 105p |
| Sporothrix Set | 100p |
| Hespar Set | 100p |
| Vauban Prime Set | 95p |
| Dual Kamas Prime Set | 90p |
| Afuris Prime Set | 82p |
| Kronen Prime Set | 80p |
| Limbo Prime Set | 72p |
| Nyx Prime Set | 72p |
| Chroma Prime Set | 71p |
| Wukong Prime Set | 70p |
| Carrier Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Bonewidow Set | 70p |
| Nova Prime Set | 70p |
| Mirage Prime Set | 70p |
| Titania Prime Set | 66p |
| Nami Skyla Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Rhino Prime Set | 65p |
| Kogake Prime Set | 65p |
| Nekros Prime Set | 65p |
| Dethcube Prime Set | 62p |
| Loki Prime Set | 61p |
| Frost Prime Set | 60p |
| Vectis Prime Set | 60p |
| Oberon Prime Set | 60p |
| Trinity Prime Set | 60p |
| Xiphos Set | 60p |
| Tekko Prime Set | 60p |
| Octavia Prime Set | 60p |
| Carmine Penta Set | 60p |
| Nidus Prime Set | 60p |
| Khora Prime Set | 60p |
| Baza Prime Set | 56p |
| Zephyr Prime Set | 56p |
| Corinth Prime Set | 56p |
| Gara Prime Set | 56p |
| Saryn Prime Set | 55p |
| Mag Prime Set | 55p |
| Bo Prime Set | 55p |
| Banshee Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Equinox Prime Set | 55p |
| Nezha Prime Set | 55p |
| Phantasma Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
