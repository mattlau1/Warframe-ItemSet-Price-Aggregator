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
**Last Updated:** 2026-01-12 15:15 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 321p |
| Braton Vandal Set | 310p |
| Vauban Prime Set | 126p |
| Akstiletto Prime Set | 110p |
| Hespar Set | 101p |
| Dual Kamas Prime Set | 100p |
| Spira Prime Set | 100p |
| Nami Skyla Prime Set | 90p |
| Arum Spinosa Set | 90p |
| Limbo Prime Set | 83p |
| Kronen Prime Set | 80p |
| Sporothrix Set | 80p |
| Aksomati Prime Set | 75p |
| Nyx Prime Set | 75p |
| Akjagara Prime Set | 75p |
| Nekros Prime Set | 73p |
| Hydroid Prime Set | 70p |
| Saryn Prime Set | 70p |
| Wukong Prime Set | 70p |
| Boar Prime Set | 70p |
| Carrier Prime Set | 70p |
| Tekko Prime Set | 70p |
| Khora Prime Set | 70p |
| Valkyr Prime Set | 66p |
| Nova Prime Set | 66p |
| Mirage Prime Set | 66p |
| Garuda Prime Set | 66p |
| Frost Prime Set | 65p |
| Vectis Prime Set | 65p |
| Kogake Prime Set | 65p |
| Ballistica Prime Set | 65p |
| Dethcube Prime Set | 65p |
| Loki Prime Set | 65p |
| Akbolto Prime Set | 63p |
| Atlas Prime Set | 63p |
| Octavia Prime Set | 63p |
| Carmine Penta Set | 63p |
| Rhino Prime Set | 61p |
| Titania Prime Set | 61p |
| Afuris Prime Set | 61p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Venka Prime Set | 60p |
| Baza Prime Set | 60p |
| Chroma Prime Set | 60p |
| Corinth Prime Set | 60p |
| Gara Prime Set | 60p |
| Nidus Prime Set | 60p |
| Cinta Set | 60p |
| Wyrm Prime Set | 59p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)