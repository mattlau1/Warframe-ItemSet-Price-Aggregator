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
**Last Updated:** 2026-01-15 02:52 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 336p |
| Braton Vandal Set | 313p |
| Vauban Prime Set | 135p |
| Akstiletto Prime Set | 115p |
| Dual Kamas Prime Set | 110p |
| Spira Prime Set | 105p |
| Arum Spinosa Set | 101p |
| Hespar Set | 90p |
| Nami Skyla Prime Set | 85p |
| Limbo Prime Set | 82p |
| Sporothrix Set | 82p |
| Akjagara Prime Set | 80p |
| Afuris Prime Set | 80p |
| Tekko Prime Set | 78p |
| Akbolto Prime Set | 75p |
| Nyx Prime Set | 75p |
| Nekros Prime Set | 75p |
| Dethcube Prime Set | 73p |
| Hydroid Prime Set | 72p |
| Boar Prime Set | 70p |
| Carrier Prime Set | 70p |
| Kronen Prime Set | 70p |
| Mirage Prime Set | 70p |
| Prisma Shade Set | 70p |
| Khora Prime Set | 68p |
| Wukong Prime Set | 67p |
| Aksomati Prime Set | 67p |
| Titania Prime Set | 67p |
| Loki Prime Set | 67p |
| Garuda Prime Set | 67p |
| Kogake Prime Set | 66p |
| Frost Prime Set | 65p |
| Rhino Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Nova Prime Set | 65p |
| Carmine Penta Set | 65p |
| Nidus Prime Set | 65p |
| Saryn Prime Set | 62p |
| Oberon Prime Set | 62p |
| Chroma Prime Set | 62p |
| Atlas Prime Set | 61p |
| Octavia Prime Set | 61p |
| Vectis Prime Set | 60p |
| Bo Prime Set | 60p |
| Trinity Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Corinth Prime Set | 60p |
| Gara Prime Set | 60p |
| Mag Prime Set | 58p |
| Sybaris Prime Set | 58p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)