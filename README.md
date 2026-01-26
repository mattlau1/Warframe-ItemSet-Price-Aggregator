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
**Last Updated:** 2026-01-26 18:18 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 300p |
| Braton Vandal Set | 275p |
| Vauban Prime Set | 143p |
| Akstiletto Prime Set | 111p |
| Hespar Set | 110p |
| Dual Kamas Prime Set | 91p |
| Sporothrix Set | 90p |
| Spira Prime Set | 85p |
| Afuris Prime Set | 81p |
| Aksomati Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Akbolto Prime Set | 79p |
| Arum Spinosa Set | 77p |
| Kronen Prime Set | 76p |
| Tekko Prime Set | 75p |
| Nyx Prime Set | 75p |
| Limbo Prime Set | 71p |
| Akjagara Prime Set | 71p |
| Nekros Prime Set | 70p |
| Corinth Prime Set | 68p |
| Wukong Prime Set | 66p |
| Dethcube Prime Set | 66p |
| Titania Prime Set | 66p |
| Nova Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Mirage Prime Set | 65p |
| Carmine Penta Set | 65p |
| Nidus Prime Set | 65p |
| Loki Prime Set | 63p |
| Saryn Prime Set | 61p |
| Vectis Prime Set | 61p |
| Oberon Prime Set | 61p |
| Carrier Prime Set | 61p |
| Atlas Prime Set | 61p |
| Gara Prime Set | 61p |
| Khora Prime Set | 61p |
| Frost Prime Set | 60p |
| Latron Prime Set | 60p |
| Rhino Prime Set | 60p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Kogake Prime Set | 60p |
| Cortege Set | 60p |
| Morgha Set | 60p |
| Octavia Prime Set | 60p |
| Garuda Prime Set | 60p |
| Baza Prime Set | 58p |
| Mag Prime Set | 56p |
| Chroma Prime Set | 56p |
| Banshee Prime Set | 56p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)