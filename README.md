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
**Last Updated:** 2026-06-08 18:22 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 107p |
| Vectis Prime Set | 95p |
| Kronen Prime Set | 93p |
| Vauban Prime Set | 86p |
| Limbo Prime Set | 85p |
| Nami Skyla Prime Set | 85p |
| Afuris Prime Set | 85p |
| Akbolto Prime Set | 80p |
| Spira Prime Set | 80p |
| Nekros Prime Set | 80p |
| Hydroid Prime Set | 77p |
| Nidus Prime Set | 76p |
| Khora Prime Set | 76p |
| Ballistica Prime Set | 75p |
| Carrier Prime Set | 75p |
| Corinth Prime Set | 71p |
| Frost Prime Set | 70p |
| Saryn Prime Set | 70p |
| Oberon Prime Set | 70p |
| Kogake Prime Set | 70p |
| Mirage Prime Set | 70p |
| Carmine Penta Set | 70p |
| Scourge Prime Set | 70p |
| Garuda Prime Set | 70p |
| Aksomati Prime Set | 65p |
| Chroma Prime Set | 65p |
| Loki Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Gara Prime Set | 65p |
| Destreza Prime Set | 64p |
| Mag Prime Set | 63p |
| Valkyr Prime Set | 62p |
| Dual Kamas Prime Set | 61p |
| Boar Prime Set | 61p |
| Titania Prime Set | 61p |
| Octavia Prime Set | 61p |
| Latron Prime Set | 60p |
| Ninkondi Prime Set | 60p |
| Wukong Prime Set | 60p |
| Bo Prime Set | 60p |
| Baza Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Glaive Prime Set | 60p |
| Xiphos Set | 60p |
| Banshee Prime Set | 60p |
| Mesa Prime Set | 60p |
| Nezha Prime Set | 60p |
| Tekko Prime Set | 59p |
| Helios Prime Set | 56p |
| Wisp Prime Set | 56p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
