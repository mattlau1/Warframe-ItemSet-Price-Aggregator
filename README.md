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
**Last Updated:** 2026-02-20 08:34 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 280p |
| Lato Vandal Set | 250p |
| Dual Kamas Prime Set | 101p |
| Akstiletto Prime Set | 100p |
| Vauban Prime Set | 100p |
| Arum Spinosa Set | 90p |
| Sporothrix Set | 88p |
| Hespar Set | 81p |
| Kronen Prime Set | 80p |
| Carmine Penta Set | 75p |
| Nyx Prime Set | 72p |
| Afuris Prime Set | 72p |
| Rhino Prime Set | 70p |
| Wukong Prime Set | 70p |
| Carrier Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Limbo Prime Set | 70p |
| Corinth Prime Set | 70p |
| Nidus Prime Set | 70p |
| Hydroid Prime Set | 66p |
| Nova Prime Set | 66p |
| Titania Prime Set | 65p |
| Chroma Prime Set | 65p |
| Mirage Prime Set | 65p |
| Gara Prime Set | 63p |
| Frost Prime Set | 61p |
| Vectis Prime Set | 61p |
| Oberon Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Nami Skyla Prime Set | 60p |
| Loki Prime Set | 60p |
| Nekros Prime Set | 60p |
| Mag Prime Set | 56p |
| Boar Prime Set | 56p |
| Wyrm Prime Set | 55p |
| Atlas Prime Set | 55p |
| Nezha Prime Set | 55p |
| Octavia Prime Set | 55p |
| Khora Prime Set | 55p |
| Baza Prime Set | 51p |
| Valkyr Prime Set | 51p |
| Saryn Prime Set | 50p |
| Bo Prime Set | 50p |
| Kogake Prime Set | 50p |
| Trinity Prime Set | 50p |
| Aksomati Prime Set | 50p |
| Xiphos Set | 50p |
| Spira Prime Set | 50p |
| Cortege Set | 50p |
| Zephyr Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
