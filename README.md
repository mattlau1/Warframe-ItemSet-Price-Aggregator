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
**Last Updated:** 2026-04-29 02:28 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 101p |
| Kronen Prime Set | 90p |
| Vauban Prime Set | 85p |
| Vectis Prime Set | 83p |
| Limbo Prime Set | 81p |
| Afuris Prime Set | 81p |
| Carmine Penta Set | 80p |
| Hydroid Prime Set | 77p |
| Xiphos Set | 77p |
| Titania Prime Set | 76p |
| Wukong Prime Set | 75p |
| Aksomati Prime Set | 75p |
| Spira Prime Set | 75p |
| Chroma Prime Set | 75p |
| Nekros Prime Set | 75p |
| Nidus Prime Set | 75p |
| Akjagara Prime Set | 72p |
| Akbolto Prime Set | 71p |
| Rhino Prime Set | 70p |
| Ballistica Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Cortege Set | 70p |
| Nyx Prime Set | 70p |
| Mirage Prime Set | 70p |
| Garuda Prime Set | 70p |
| Khora Prime Set | 70p |
| Voruna Prime Set | 70p |
| Frost Prime Set | 65p |
| Destreza Prime Set | 65p |
| Akstiletto Prime Set | 65p |
| Loki Prime Set | 65p |
| Morgha Set | 65p |
| Octavia Prime Set | 65p |
| Gara Prime Set | 65p |
| Corinth Prime Set | 62p |
| Kogake Prime Set | 61p |
| Bonewidow Set | 61p |
| Prisma Shade Set | 61p |
| Akvasto Prime Set | 60p |
| Ankyros Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Banshee Prime Set | 60p |
| Scourge Prime Set | 60p |
| Cinta Set | 60p |
| Phantasma Prime Set | 58p |
| Boltor Prime Set | 57p |
| Oberon Prime Set | 56p |
| Boar Prime Set | 56p |
| Saryn Prime Set | 55p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
