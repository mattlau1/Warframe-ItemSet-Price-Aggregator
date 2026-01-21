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
**Last Updated:** 2026-01-21 09:21 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 301p |
| Lato Vandal Set | 280p |
| Vauban Prime Set | 130p |
| Dual Kamas Prime Set | 120p |
| Akstiletto Prime Set | 113p |
| Arum Spinosa Set | 100p |
| Hespar Set | 100p |
| Aksomati Prime Set | 85p |
| Spira Prime Set | 80p |
| Sporothrix Set | 80p |
| Tekko Prime Set | 77p |
| Limbo Prime Set | 76p |
| Boar Prime Set | 75p |
| Dethcube Prime Set | 75p |
| Nami Skyla Prime Set | 75p |
| Afuris Prime Set | 75p |
| Kronen Prime Set | 72p |
| Nekros Prime Set | 72p |
| Wukong Prime Set | 70p |
| Titania Prime Set | 70p |
| Khora Prime Set | 70p |
| Hydroid Prime Set | 69p |
| Carrier Prime Set | 68p |
| Nova Prime Set | 68p |
| Nyx Prime Set | 68p |
| Akjagara Prime Set | 67p |
| Mirage Prime Set | 66p |
| Nidus Prime Set | 66p |
| Saryn Prime Set | 65p |
| Latron Prime Set | 65p |
| Oberon Prime Set | 65p |
| Bo Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Octavia Prime Set | 65p |
| Gara Prime Set | 65p |
| Garuda Prime Set | 65p |
| Frost Prime Set | 63p |
| Ballistica Prime Set | 62p |
| Atlas Prime Set | 62p |
| Chroma Prime Set | 62p |
| Rhino Prime Set | 61p |
| Mag Prime Set | 61p |
| Vectis Prime Set | 60p |
| Kogake Prime Set | 60p |
| Banshee Prime Set | 60p |
| Loki Prime Set | 60p |
| Corinth Prime Set | 60p |
| Bonewidow Set | 57p |
| Akbolto Prime Set | 56p |
| Nezha Prime Set | 56p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)