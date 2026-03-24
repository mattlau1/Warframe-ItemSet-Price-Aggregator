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
**Last Updated:** 2026-03-24 08:44 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 210p |
| Lato Vandal Set | 202p |
| Hespar Set | 98p |
| Kronen Prime Set | 90p |
| Arum Spinosa Set | 90p |
| Limbo Prime Set | 85p |
| Dual Kamas Prime Set | 80p |
| Vauban Prime Set | 80p |
| Wukong Prime Set | 77p |
| Afuris Prime Set | 76p |
| Akstiletto Prime Set | 75p |
| Chroma Prime Set | 75p |
| Rhino Prime Set | 71p |
| Vectis Prime Set | 70p |
| Titania Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Nyx Prime Set | 70p |
| Nekros Prime Set | 70p |
| Gara Prime Set | 70p |
| Octavia Prime Set | 69p |
| Bo Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Saryn Prime Set | 65p |
| Latron Prime Set | 65p |
| Boar Prime Set | 65p |
| Carrier Prime Set | 65p |
| Spira Prime Set | 65p |
| Khora Prime Set | 65p |
| Aksomati Prime Set | 62p |
| Tipedo Prime Set | 61p |
| Mirage Prime Set | 61p |
| Corinth Prime Set | 61p |
| Strun Prime Set | 61p |
| Oberon Prime Set | 60p |
| Boltor Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Sporothrix Set | 60p |
| Loki Prime Set | 60p |
| Nova Prime Set | 60p |
| Carmine Penta Set | 60p |
| Scourge Prime Set | 60p |
| Garuda Prime Set | 60p |
| Cinta Set | 60p |
| Bonewidow Set | 57p |
| Mag Prime Set | 56p |
| Banshee Prime Set | 56p |
| Ankyros Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Nezha Prime Set | 55p |
| Nidus Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
