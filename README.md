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
**Last Updated:** 2026-04-20 16:59 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 100p |
| Kronen Prime Set | 97p |
| Vectis Prime Set | 85p |
| Akbolto Prime Set | 85p |
| Afuris Prime Set | 85p |
| Vauban Prime Set | 82p |
| Limbo Prime Set | 81p |
| Kogake Prime Set | 80p |
| Aksomati Prime Set | 80p |
| Spira Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Chroma Prime Set | 80p |
| Carmine Penta Set | 80p |
| Voruna Prime Set | 80p |
| Hydroid Prime Set | 76p |
| Titania Prime Set | 76p |
| Wukong Prime Set | 75p |
| Ballistica Prime Set | 75p |
| Mirage Prime Set | 75p |
| Akstiletto Prime Set | 74p |
| Akjagara Prime Set | 72p |
| Rhino Prime Set | 71p |
| Nyx Prime Set | 71p |
| Nekros Prime Set | 71p |
| Destreza Prime Set | 70p |
| Octavia Prime Set | 69p |
| Corinth Prime Set | 68p |
| Gara Prime Set | 68p |
| Nidus Prime Set | 67p |
| Mag Prime Set | 65p |
| Boar Prime Set | 65p |
| Carrier Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Scourge Prime Set | 65p |
| Khora Prime Set | 64p |
| Saryn Prime Set | 62p |
| Bo Prime Set | 61p |
| Cinta Set | 61p |
| Frost Prime Set | 60p |
| Dual Kamas Prime Set | 60p |
| Latron Prime Set | 60p |
| Oberon Prime Set | 60p |
| Akvasto Prime Set | 60p |
| Panthera Prime Set | 60p |
| Bonewidow Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Garuda Prime Set | 60p |
| Prisma Shade Set | 60p |
| Wyrm Prime Set | 58p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
