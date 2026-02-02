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
**Last Updated:** 2026-02-02 16:32 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 282p |
| Braton Vandal Set | 280p |
| Vauban Prime Set | 130p |
| Dual Kamas Prime Set | 107p |
| Akstiletto Prime Set | 100p |
| Hespar Set | 100p |
| Arum Spinosa Set | 96p |
| Limbo Prime Set | 80p |
| Spira Prime Set | 80p |
| Sporothrix Set | 80p |
| Afuris Prime Set | 76p |
| Nami Skyla Prime Set | 75p |
| Aksomati Prime Set | 71p |
| Akbolto Prime Set | 71p |
| Wukong Prime Set | 70p |
| Dethcube Prime Set | 70p |
| Nova Prime Set | 70p |
| Nyx Prime Set | 70p |
| Akjagara Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nekros Prime Set | 70p |
| Titania Prime Set | 69p |
| Kronen Prime Set | 67p |
| Rhino Prime Set | 65p |
| Boar Prime Set | 65p |
| Boltor Prime Set | 65p |
| Xiphos Set | 65p |
| Tekko Prime Set | 65p |
| Nidus Prime Set | 65p |
| Chroma Prime Set | 64p |
| Corinth Prime Set | 63p |
| Gara Prime Set | 62p |
| Frost Prime Set | 61p |
| Hydroid Prime Set | 61p |
| Carrier Prime Set | 61p |
| Carmine Penta Set | 61p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Atlas Prime Set | 60p |
| Loki Prime Set | 60p |
| Octavia Prime Set | 60p |
| Nautilus Set | 60p |
| Khora Prime Set | 60p |
| Vectis Prime Set | 58p |
| Mag Prime Set | 58p |
| Banshee Prime Set | 58p |
| Scourge Prime Set | 56p |
| Saryn Prime Set | 55p |
| Latron Prime Set | 55p |
| Trinity Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
