# 📊 WarframeMarket-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/WarframeMarket-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
git clone https://github.com/mattlau1/WarframeMarket-ItemSet-Price-Aggregator.git
cd WarframeMarket-ItemSet-Price-Aggregator
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
This project uses a specific Git-based version of the Warframe Market API client.
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
**Last Updated:** 2025-12-31 16:13 UTC

```text
Braton Vandal Set: 251p
Lato Vandal Set: 250p
Akstiletto Prime Set: 120p
Vauban Prime Set: 120p
Dual Kamas Prime Set: 110p
Spira Prime Set: 96p
Nami Skyla Prime Set: 95p
Hespar Set: 90p
Sporothrix Set: 81p
Kronen Prime Set: 80p
Akjagara Prime Set: 80p
Valkyr Prime Set: 79p
Vectis Prime Set: 75p
Dethcube Prime Set: 75p
Limbo Prime Set: 75p
Aksomati Prime Set: 72p
Saryn Prime Set: 71p
Hydroid Prime Set: 70p
Arum Spinosa Set: 70p
Nekros Prime Set: 70p
Wukong Prime Set: 65p
Kogake Prime Set: 65p
Akbolto Prime Set: 65p
Loki Prime Set: 65p
Frost Prime Set: 62p
Nikana Prime Set: 62p
Nyx Prime Set: 62p
Oberon Prime Set: 61p
Bo Prime Set: 61p
Ballistica Prime Set: 61p
Mirage Prime Set: 61p
Carmine Penta Set: 61p
Afuris Prime Set: 61p
Venka Prime Set: 60p
Carrier Prime Set: 60p
Wyrm Prime Set: 60p
Xiphos Set: 60p
Tipedo Prime Set: 60p
Tekko Prime Set: 60p
Cortege Set: 60p
Chroma Prime Set: 60p
Octavia Prime Set: 60p
Scourge Prime Set: 60p
Garuda Prime Set: 60p
Khora Prime Set: 60p
Titania Prime Set: 59p
Rhino Prime Set: 58p
Nidus Prime Set: 57p
Nova Prime Set: 56p
Mag Prime Set: 55p
... (see out.txt for full list)
```
[//]: # (PRICE_END)