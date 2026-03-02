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
**Last Updated:** 2026-03-02 20:31 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 229p |
| Lato Vandal Set | 219p |
| Dual Kamas Prime Set | 115p |
| Kronen Prime Set | 95p |
| Hespar Set | 95p |
| Sporothrix Set | 90p |
| Akstiletto Prime Set | 85p |
| Nami Skyla Prime Set | 80p |
| Arum Spinosa Set | 80p |
| Vauban Prime Set | 76p |
| Akbolto Prime Set | 75p |
| Mirage Prime Set | 75p |
| Afuris Prime Set | 75p |
| Corinth Prime Set | 71p |
| Wukong Prime Set | 70p |
| Titania Prime Set | 70p |
| Limbo Prime Set | 70p |
| Spira Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nova Prime Set | 70p |
| Nyx Prime Set | 70p |
| Nekros Prime Set | 70p |
| Carmine Penta Set | 70p |
| Nidus Prime Set | 70p |
| Akjagara Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Kogake Prime Set | 65p |
| Carrier Prime Set | 65p |
| Banshee Prime Set | 65p |
| Gara Prime Set | 65p |
| Vectis Prime Set | 62p |
| Boltor Prime Set | 62p |
| Cinta Set | 62p |
| Aksomati Prime Set | 61p |
| Frost Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Strun Wraith Set | 60p |
| Trinity Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Equinox Prime Set | 60p |
| Octavia Prime Set | 60p |
| Khora Prime Set | 60p |
| Soma Prime Set | 56p |
| Ninkondi Prime Set | 55p |
| Ankyros Prime Set | 55p |
| Baza Prime Set | 55p |
| Sybaris Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
