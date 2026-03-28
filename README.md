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
**Last Updated:** 2026-03-28 08:33 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 100p |
| Wukong Prime Set | 80p |
| Limbo Prime Set | 77p |
| Kronen Prime Set | 77p |
| Carrier Prime Set | 75p |
| Nekros Prime Set | 74p |
| Dual Kamas Prime Set | 71p |
| Braton Vandal Set | 71p |
| Titania Prime Set | 71p |
| Chroma Prime Set | 71p |
| Vauban Prime Set | 71p |
| Mirage Prime Set | 71p |
| Vectis Prime Set | 70p |
| Rhino Prime Set | 70p |
| Zephyr Prime Set | 70p |
| Gara Prime Set | 70p |
| Hydroid Prime Set | 68p |
| Boar Prime Set | 68p |
| Oberon Prime Set | 65p |
| Bo Prime Set | 65p |
| Spira Prime Set | 65p |
| Nyx Prime Set | 65p |
| Octavia Prime Set | 65p |
| Nami Skyla Prime Set | 62p |
| Saryn Prime Set | 60p |
| Latron Prime Set | 60p |
| Kogake Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Xiphos Set | 60p |
| Tipedo Prime Set | 60p |
| Loki Prime Set | 60p |
| Carmine Penta Set | 60p |
| Nidus Prime Set | 60p |
| Khora Prime Set | 60p |
| Afuris Prime Set | 60p |
| Frost Prime Set | 56p |
| Wyrm Prime Set | 56p |
| Akjagara Prime Set | 56p |
| Mag Prime Set | 55p |
| Aksomati Prime Set | 55p |
| Inaros Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Cortege Set | 55p |
| Banshee Prime Set | 55p |
| Equinox Prime Set | 55p |
| Nezha Prime Set | 55p |
| Morgha Set | 55p |
| Phantasma Prime Set | 55p |
| Akarius Prime Set | 55p |
| Hildryn Prime Set | 53p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
