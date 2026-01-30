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
**Last Updated:** 2026-01-30 11:19 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 288p |
| Lato Vandal Set | 280p |
| Vauban Prime Set | 130p |
| Hespar Set | 117p |
| Dual Kamas Prime Set | 111p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 100p |
| Limbo Prime Set | 80p |
| Spira Prime Set | 80p |
| Akjagara Prime Set | 80p |
| Akbolto Prime Set | 76p |
| Tekko Prime Set | 75p |
| Afuris Prime Set | 75p |
| Nekros Prime Set | 72p |
| Wukong Prime Set | 71p |
| Kronen Prime Set | 71p |
| Nyx Prime Set | 71p |
| Rhino Prime Set | 70p |
| Dethcube Prime Set | 70p |
| Titania Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nova Prime Set | 67p |
| Nidus Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Boar Prime Set | 65p |
| Kogake Prime Set | 65p |
| Carrier Prime Set | 65p |
| Xiphos Set | 65p |
| Chroma Prime Set | 65p |
| Gara Prime Set | 65p |
| Sporothrix Set | 64p |
| Aksomati Prime Set | 62p |
| Octavia Prime Set | 62p |
| Frost Prime Set | 61p |
| Vectis Prime Set | 61p |
| Oberon Prime Set | 61p |
| Carmine Penta Set | 61p |
| Latron Prime Set | 60p |
| Bo Prime Set | 60p |
| Banshee Prime Set | 60p |
| Loki Prime Set | 60p |
| Corinth Prime Set | 60p |
| Scourge Prime Set | 60p |
| Khora Prime Set | 60p |
| Baruuk Prime Set | 60p |
| Mag Prime Set | 56p |
| Trinity Prime Set | 56p |
| Boltor Prime Set | 55p |
| Ankyros Prime Set | 55p |
| Valkyr Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)