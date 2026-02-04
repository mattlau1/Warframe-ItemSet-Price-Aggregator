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
**Last Updated:** 2026-02-04 12:45 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 276p |
| Lato Vandal Set | 261p |
| Vauban Prime Set | 130p |
| Dual Kamas Prime Set | 120p |
| Hespar Set | 120p |
| Akstiletto Prime Set | 100p |
| Limbo Prime Set | 80p |
| Arum Spinosa Set | 80p |
| Sporothrix Set | 80p |
| Akjagara Prime Set | 80p |
| Titania Prime Set | 75p |
| Carmine Penta Set | 75p |
| Afuris Prime Set | 75p |
| Wukong Prime Set | 72p |
| Mirage Prime Set | 72p |
| Aksomati Prime Set | 71p |
| Nova Prime Set | 71p |
| Dethcube Prime Set | 70p |
| Tekko Prime Set | 70p |
| Nyx Prime Set | 70p |
| Nekros Prime Set | 70p |
| Hydroid Prime Set | 67p |
| Boar Prime Set | 66p |
| Rhino Prime Set | 65p |
| Carrier Prime Set | 65p |
| Akbolto Prime Set | 65p |
| Chroma Prime Set | 65p |
| Loki Prime Set | 65p |
| Nidus Prime Set | 65p |
| Gara Prime Set | 63p |
| Oberon Prime Set | 61p |
| Frost Prime Set | 60p |
| Vectis Prime Set | 60p |
| Bo Prime Set | 60p |
| Baza Prime Set | 60p |
| Atlas Prime Set | 60p |
| Banshee Prime Set | 60p |
| Corinth Prime Set | 60p |
| Nezha Prime Set | 60p |
| Scourge Prime Set | 60p |
| Khora Prime Set | 60p |
| Saryn Prime Set | 58p |
| Kronen Prime Set | 57p |
| Valkyr Prime Set | 56p |
| Latron Prime Set | 55p |
| Mag Prime Set | 55p |
| Boltor Prime Set | 55p |
| Kogake Prime Set | 55p |
| Ballistica Prime Set | 55p |
| Wyrm Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
