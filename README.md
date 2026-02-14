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
**Last Updated:** 2026-02-14 12:36 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 260p |
| Braton Vandal Set | 250p |
| Vauban Prime Set | 131p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 96p |
| Hespar Set | 86p |
| Akbolto Prime Set | 75p |
| Limbo Prime Set | 75p |
| Aksomati Prime Set | 70p |
| Titania Prime Set | 70p |
| Nova Prime Set | 70p |
| Nyx Prime Set | 70p |
| Afuris Prime Set | 70p |
| Kronen Prime Set | 67p |
| Nekros Prime Set | 67p |
| Hydroid Prime Set | 65p |
| Wukong Prime Set | 65p |
| Xiphos Set | 65p |
| Chroma Prime Set | 65p |
| Mirage Prime Set | 65p |
| Nidus Prime Set | 65p |
| Rhino Prime Set | 64p |
| Bo Prime Set | 61p |
| Tekko Prime Set | 61p |
| Loki Prime Set | 61p |
| Frost Prime Set | 60p |
| Vectis Prime Set | 60p |
| Oberon Prime Set | 60p |
| Boar Prime Set | 60p |
| Kogake Prime Set | 60p |
| Spira Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Carrier Prime Set | 58p |
| Nami Skyla Prime Set | 58p |
| Wyrm Prime Set | 56p |
| Banshee Prime Set | 56p |
| Octavia Prime Set | 56p |
| Latron Prime Set | 55p |
| Dethcube Prime Set | 55p |
| Tipedo Prime Set | 55p |
| Atlas Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Scourge Prime Set | 55p |
| Khora Prime Set | 55p |
| Nezha Prime Set | 54p |
| Trinity Prime Set | 53p |
| Saryn Prime Set | 52p |
| Ballistica Prime Set | 52p |
| Mag Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
