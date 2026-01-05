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
**Last Updated:** 2026-01-05 15:13 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 280p |
| Lato Vandal Set | 275p |
| Akstiletto Prime Set | 120p |
| Vauban Prime Set | 120p |
| Dual Kamas Prime Set | 111p |
| Arum Spinosa Set | 110p |
| Hespar Set | 101p |
| Spira Prime Set | 97p |
| Nami Skyla Prime Set | 92p |
| Sporothrix Set | 90p |
| Akjagara Prime Set | 81p |
| Valkyr Prime Set | 80p |
| Nekros Prime Set | 80p |
| Aksomati Prime Set | 75p |
| Limbo Prime Set | 75p |
| Kronen Prime Set | 75p |
| Mirage Prime Set | 75p |
| Vectis Prime Set | 72p |
| Dethcube Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Saryn Prime Set | 70p |
| Wukong Prime Set | 70p |
| Carrier Prime Set | 70p |
| Sybaris Prime Set | 70p |
| Nikana Prime Set | 70p |
| Nyx Prime Set | 70p |
| Kogake Prime Set | 67p |
| Khora Prime Set | 67p |
| Loki Prime Set | 66p |
| Titania Prime Set | 65p |
| Tekko Prime Set | 65p |
| Chroma Prime Set | 65p |
| Nova Prime Set | 65p |
| Garuda Prime Set | 65p |
| Frost Prime Set | 63p |
| Carmine Penta Set | 62p |
| Oberon Prime Set | 61p |
| Xiphos Set | 61p |
| Rhino Prime Set | 60p |
| Bo Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Venka Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Corinth Prime Set | 60p |
| Octavia Prime Set | 60p |
| Gara Prime Set | 60p |
| Scourge Prime Set | 60p |
| Afuris Prime Set | 60p |
| Baza Prime Set | 57p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)