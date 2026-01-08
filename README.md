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
**Last Updated:** 2026-01-08 07:15 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 275p |
| Braton Vandal Set | 240p |
| Vauban Prime Set | 126p |
| Akstiletto Prime Set | 116p |
| Dual Kamas Prime Set | 115p |
| Arum Spinosa Set | 110p |
| Spira Prime Set | 100p |
| Sporothrix Set | 90p |
| Hespar Set | 90p |
| Akjagara Prime Set | 85p |
| Limbo Prime Set | 80p |
| Kronen Prime Set | 77p |
| Nami Skyla Prime Set | 76p |
| Valkyr Prime Set | 75p |
| Carmine Penta Set | 75p |
| Aksomati Prime Set | 71p |
| Saryn Prime Set | 70p |
| Wukong Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nekros Prime Set | 70p |
| Garuda Prime Set | 70p |
| Hydroid Prime Set | 68p |
| Titania Prime Set | 68p |
| Dethcube Prime Set | 67p |
| Vectis Prime Set | 66p |
| Carrier Prime Set | 66p |
| Frost Prime Set | 65p |
| Loki Prime Set | 65p |
| Nova Prime Set | 65p |
| Nyx Prime Set | 65p |
| Kogake Prime Set | 63p |
| Atlas Prime Set | 62p |
| Chroma Prime Set | 62p |
| Rhino Prime Set | 61p |
| Bo Prime Set | 60p |
| Nezha Prime Set | 60p |
| Gara Prime Set | 60p |
| Khora Prime Set | 60p |
| Afuris Prime Set | 60p |
| Mag Prime Set | 59p |
| Ballistica Prime Set | 59p |
| Oberon Prime Set | 56p |
| Nikana Prime Set | 56p |
| Nidus Prime Set | 56p |
| Latron Prime Set | 55p |
| Boar Prime Set | 55p |
| Trinity Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Wyrm Prime Set | 55p |
| Inaros Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)