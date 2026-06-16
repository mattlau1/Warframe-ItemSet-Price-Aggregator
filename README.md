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
**Last Updated:** 2026-06-16 16:40 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 104p |
| Hespar Set | 95p |
| Vauban Prime Set | 90p |
| Spira Prime Set | 86p |
| Limbo Prime Set | 85p |
| Kronen Prime Set | 85p |
| Mirage Prime Set | 81p |
| Hydroid Prime Set | 80p |
| Aksomati Prime Set | 80p |
| Titania Prime Set | 77p |
| Nidus Prime Set | 77p |
| Nekros Prime Set | 76p |
| Carrier Prime Set | 75p |
| Akbolto Prime Set | 75p |
| Afuris Prime Set | 75p |
| Banshee Prime Set | 71p |
| Octavia Prime Set | 71p |
| Chroma Prime Set | 70p |
| Gara Prime Set | 70p |
| Khora Prime Set | 70p |
| Saryn Prime Set | 66p |
| Oberon Prime Set | 66p |
| Boar Prime Set | 66p |
| Wyrm Prime Set | 66p |
| Loki Prime Set | 66p |
| Frost Prime Set | 65p |
| Mag Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Nami Skyla Prime Set | 65p |
| Bonewidow Set | 65p |
| Garuda Prime Set | 65p |
| Wukong Prime Set | 63p |
| Carmine Penta Set | 61p |
| Dual Kamas Prime Set | 60p |
| Latron Prime Set | 60p |
| Ninkondi Prime Set | 60p |
| Bo Prime Set | 60p |
| Baza Prime Set | 60p |
| Mesa Prime Set | 60p |
| Corinth Prime Set | 60p |
| Scourge Prime Set | 60p |
| Baruuk Prime Set | 60p |
| Cinta Set | 60p |
| Akarius Prime Set | 57p |
| Helios Prime Set | 56p |
| Nautilus Set | 56p |
| Hildryn Prime Set | 56p |
| Wisp Prime Set | 56p |
| Glaive Prime Set | 55p |
| Tipedo Prime Set | 55p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
