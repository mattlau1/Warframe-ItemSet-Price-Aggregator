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
**Last Updated:** 2026-06-29 18:07 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 125p |
| Vectis Prime Set | 106p |
| Destreza Prime Set | 93p |
| Vauban Prime Set | 90p |
| Limbo Prime Set | 80p |
| Spira Prime Set | 80p |
| Nekros Prime Set | 80p |
| Hespar Set | 80p |
| Hydroid Prime Set | 75p |
| Kronen Prime Set | 75p |
| Carmine Penta Set | 75p |
| Nidus Prime Set | 74p |
| Carrier Prime Set | 70p |
| Garuda Prime Set | 70p |
| Octavia Prime Set | 67p |
| Loki Prime Set | 65p |
| Mirage Prime Set | 65p |
| Khora Prime Set | 65p |
| Styanax Prime Set | 65p |
| Afentis Prime Set | 65p |
| Frost Prime Set | 63p |
| Saryn Prime Set | 61p |
| Bo Prime Set | 61p |
| Boar Prime Set | 61p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Akstiletto Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Nami Skyla Prime Set | 60p |
| Chroma Prime Set | 60p |
| Banshee Prime Set | 60p |
| Corinth Prime Set | 60p |
| Scourge Prime Set | 60p |
| Cinta Set | 60p |
| Titania Prime Set | 59p |
| Helios Prime Set | 55p |
| Latron Prime Set | 55p |
| Wukong Prime Set | 55p |
| Baza Prime Set | 55p |
| Glaive Prime Set | 55p |
| Xiphos Set | 55p |
| Zephyr Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Phantasma Prime Set | 55p |
| Tekko Prime Set | 53p |
| Afuris Prime Set | 52p |
| Nova Prime Set | 51p |
| Baruuk Prime Set | 51p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
