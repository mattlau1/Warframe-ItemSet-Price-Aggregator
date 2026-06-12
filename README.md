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
**Last Updated:** 2026-06-12 21:27 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 100p |
| Hydroid Prime Set | 85p |
| Aksomati Prime Set | 85p |
| Hespar Set | 85p |
| Nekros Prime Set | 84p |
| Kronen Prime Set | 81p |
| Limbo Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Vauban Prime Set | 80p |
| Afuris Prime Set | 80p |
| Akstiletto Prime Set | 77p |
| Spira Prime Set | 77p |
| Mirage Prime Set | 76p |
| Ballistica Prime Set | 75p |
| Akbolto Prime Set | 75p |
| Banshee Prime Set | 75p |
| Garuda Prime Set | 75p |
| Corinth Prime Set | 73p |
| Dual Kamas Prime Set | 70p |
| Saryn Prime Set | 70p |
| Carrier Prime Set | 70p |
| Titania Prime Set | 70p |
| Akjagara Prime Set | 70p |
| Octavia Prime Set | 70p |
| Carmine Penta Set | 70p |
| Scourge Prime Set | 70p |
| Khora Prime Set | 70p |
| Frost Prime Set | 68p |
| Oberon Prime Set | 65p |
| Loki Prime Set | 65p |
| Mag Prime Set | 60p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Baza Prime Set | 60p |
| Gara Prime Set | 60p |
| Nidus Prime Set | 60p |
| Phantasma Prime Set | 60p |
| Cinta Set | 60p |
| Latron Prime Set | 55p |
| Wukong Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Tekko Prime Set | 55p |
| Cortege Set | 55p |
| Hildryn Prime Set | 55p |
| Wisp Prime Set | 55p |
| Panthera Prime Set | 54p |
| Helios Prime Set | 51p |
| Wyrm Prime Set | 51p |
| Destreza Prime Set | 50p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
