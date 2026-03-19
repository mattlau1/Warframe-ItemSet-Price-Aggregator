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
**Last Updated:** 2026-03-19 20:31 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 230p |
| Braton Vandal Set | 200p |
| Hespar Set | 97p |
| Dual Kamas Prime Set | 92p |
| Afuris Prime Set | 90p |
| Kronen Prime Set | 85p |
| Limbo Prime Set | 80p |
| Vauban Prime Set | 80p |
| Wukong Prime Set | 78p |
| Akstiletto Prime Set | 77p |
| Akbolto Prime Set | 75p |
| Nyx Prime Set | 74p |
| Hydroid Prime Set | 73p |
| Carrier Prime Set | 71p |
| Titania Prime Set | 71p |
| Sporothrix Set | 71p |
| Corinth Prime Set | 71p |
| Nami Skyla Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nekros Prime Set | 70p |
| Rhino Prime Set | 66p |
| Arum Spinosa Set | 66p |
| Boar Prime Set | 65p |
| Kogake Prime Set | 65p |
| Mirage Prime Set | 65p |
| Gara Prime Set | 65p |
| Nidus Prime Set | 65p |
| Latron Prime Set | 63p |
| Vectis Prime Set | 62p |
| Xiphos Set | 62p |
| Saryn Prime Set | 61p |
| Khora Prime Set | 61p |
| Frost Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Aksomati Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Banshee Prime Set | 60p |
| Loki Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Octavia Prime Set | 60p |
| Carmine Penta Set | 60p |
| Prisma Shade Set | 60p |
| Akarius Prime Set | 60p |
| Phantasma Prime Set | 59p |
| Boltor Prime Set | 55p |
| Akvasto Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Inaros Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
