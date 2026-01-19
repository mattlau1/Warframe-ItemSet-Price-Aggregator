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
**Last Updated:** 2026-01-19 21:10 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 300p |
| Braton Vandal Set | 300p |
| Dual Kamas Prime Set | 121p |
| Vauban Prime Set | 116p |
| Akstiletto Prime Set | 100p |
| Hespar Set | 100p |
| Arum Spinosa Set | 96p |
| Nami Skyla Prime Set | 90p |
| Limbo Prime Set | 83p |
| Sporothrix Set | 82p |
| Spira Prime Set | 81p |
| Akbolto Prime Set | 78p |
| Afuris Prime Set | 75p |
| Kronen Prime Set | 72p |
| Akjagara Prime Set | 71p |
| Nekros Prime Set | 71p |
| Carmine Penta Set | 71p |
| Hydroid Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Tekko Prime Set | 70p |
| Nyx Prime Set | 70p |
| Mirage Prime Set | 68p |
| Corinth Prime Set | 67p |
| Saryn Prime Set | 66p |
| Oberon Prime Set | 66p |
| Kogake Prime Set | 66p |
| Latron Prime Set | 65p |
| Dethcube Prime Set | 65p |
| Nova Prime Set | 65p |
| Nidus Prime Set | 65p |
| Garuda Prime Set | 65p |
| Khora Prime Set | 65p |
| Vectis Prime Set | 63p |
| Valkyr Prime Set | 63p |
| Frost Prime Set | 62p |
| Rhino Prime Set | 61p |
| Carrier Prime Set | 61p |
| Atlas Prime Set | 61p |
| Gara Prime Set | 61p |
| Wukong Prime Set | 60p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Venka Prime Set | 60p |
| Titania Prime Set | 60p |
| Loki Prime Set | 60p |
| Scourge Prime Set | 60p |
| Mag Prime Set | 56p |
| Ballistica Prime Set | 55p |
| Nikana Prime Set | 55p |
| Banshee Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)