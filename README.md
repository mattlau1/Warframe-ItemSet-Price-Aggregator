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
**Last Updated:** 2026-01-11 23:10 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 275p |
| Braton Vandal Set | 265p |
| Vauban Prime Set | 121p |
| Arum Spinosa Set | 115p |
| Akstiletto Prime Set | 110p |
| Spira Prime Set | 100p |
| Dual Kamas Prime Set | 90p |
| Hespar Set | 85p |
| Aksomati Prime Set | 80p |
| Sporothrix Set | 80p |
| Akjagara Prime Set | 76p |
| Nyx Prime Set | 74p |
| Nekros Prime Set | 73p |
| Valkyr Prime Set | 72p |
| Afuris Prime Set | 72p |
| Saryn Prime Set | 71p |
| Nami Skyla Prime Set | 68p |
| Limbo Prime Set | 67p |
| Hydroid Prime Set | 66p |
| Mirage Prime Set | 66p |
| Carrier Prime Set | 65p |
| Titania Prime Set | 65p |
| Nova Prime Set | 65p |
| Carmine Penta Set | 65p |
| Nidus Prime Set | 65p |
| Garuda Prime Set | 65p |
| Wukong Prime Set | 63p |
| Kronen Prime Set | 63p |
| Akbolto Prime Set | 62p |
| Frost Prime Set | 61p |
| Oberon Prime Set | 61p |
| Kogake Prime Set | 61p |
| Xiphos Set | 61p |
| Chroma Prime Set | 61p |
| Loki Prime Set | 61p |
| Octavia Prime Set | 61p |
| Rhino Prime Set | 60p |
| Baza Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Atlas Prime Set | 60p |
| Tekko Prime Set | 60p |
| Corinth Prime Set | 60p |
| Morgha Set | 60p |
| Nautilus Set | 60p |
| Khora Prime Set | 60p |
| Vectis Prime Set | 58p |
| Gara Prime Set | 58p |
| Bo Prime Set | 57p |
| Dethcube Prime Set | 57p |
| Mag Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)