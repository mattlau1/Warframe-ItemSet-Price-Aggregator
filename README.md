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
**Last Updated:** 2026-05-21 21:23 UTC

| Item Set | Median Price |
| :--- | :--- |
| Xiphos Set | 100p |
| Hespar Set | 91p |
| Vauban Prime Set | 90p |
| Afuris Prime Set | 90p |
| Vectis Prime Set | 85p |
| Kronen Prime Set | 81p |
| Hydroid Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Nekros Prime Set | 80p |
| Wukong Prime Set | 77p |
| Nidus Prime Set | 77p |
| Mirage Prime Set | 76p |
| Limbo Prime Set | 75p |
| Garuda Prime Set | 75p |
| Spira Prime Set | 71p |
| Khora Prime Set | 71p |
| Kogake Prime Set | 70p |
| Titania Prime Set | 70p |
| Chroma Prime Set | 70p |
| Carmine Penta Set | 70p |
| Latron Prime Set | 67p |
| Frost Prime Set | 66p |
| Bo Prime Set | 66p |
| Loki Prime Set | 66p |
| Corinth Prime Set | 66p |
| Prisma Shade Set | 66p |
| Oberon Prime Set | 65p |
| Bonewidow Set | 65p |
| Saryn Prime Set | 62p |
| Boar Prime Set | 61p |
| Akstiletto Prime Set | 61p |
| Valkyr Prime Set | 61p |
| Mag Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Baza Prime Set | 60p |
| Cortege Set | 60p |
| Mesa Prime Set | 60p |
| Octavia Prime Set | 60p |
| Scourge Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Strun Wraith Set | 55p |
| Aksomati Prime Set | 55p |
| Nova Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Morgha Set | 55p |
| Wisp Prime Set | 55p |
| Hildryn Prime Set | 53p |
| Ember Prime Set | 52p |
| Dethcube Prime Set | 52p |
| Ivara Prime Set | 52p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
