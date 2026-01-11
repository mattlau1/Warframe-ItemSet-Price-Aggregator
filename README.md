# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
**Last Updated:** 2026-01-11 17:09 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 310p |
| Braton Vandal Set | 307p |
| Vauban Prime Set | 125p |
| Akstiletto Prime Set | 120p |
| Arum Spinosa Set | 111p |
| Dual Kamas Prime Set | 105p |
| Spira Prime Set | 101p |
| Sporothrix Set | 90p |
| Nami Skyla Prime Set | 85p |
| Akjagara Prime Set | 85p |
| Valkyr Prime Set | 80p |
| Hespar Set | 80p |
| Nyx Prime Set | 79p |
| Aksomati Prime Set | 75p |
| Limbo Prime Set | 75p |
| Kronen Prime Set | 75p |
| Nekros Prime Set | 75p |
| Akbolto Prime Set | 74p |
| Tekko Prime Set | 71p |
| Mirage Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Saryn Prime Set | 70p |
| Nova Prime Set | 70p |
| Garuda Prime Set | 69p |
| Wukong Prime Set | 66p |
| Frost Prime Set | 65p |
| Kogake Prime Set | 65p |
| Carrier Prime Set | 65p |
| Titania Prime Set | 65p |
| Nikana Prime Set | 65p |
| Carmine Penta Set | 65p |
| Gara Prime Set | 65p |
| Khora Prime Set | 65p |
| Dethcube Prime Set | 62p |
| Loki Prime Set | 62p |
| Corinth Prime Set | 62p |
| Venka Prime Set | 61p |
| Xiphos Set | 61p |
| Atlas Prime Set | 61p |
| Vectis Prime Set | 60p |
| Oberon Prime Set | 60p |
| Trinity Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Chroma Prime Set | 60p |
| Octavia Prime Set | 60p |
| Nautilus Set | 60p |
| Nidus Prime Set | 60p |
| Boar Prime Set | 56p |
| Baza Prime Set | 56p |
| Scourge Prime Set | 56p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)