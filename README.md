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
**Last Updated:** 2026-03-27 01:53 UTC

| Item Set | Median Price |
| :--- | :--- |
| Hespar Set | 91p |
| Kronen Prime Set | 90p |
| Braton Vandal Set | 80p |
| Afuris Prime Set | 80p |
| Limbo Prime Set | 75p |
| Vauban Prime Set | 75p |
| Nami Skyla Prime Set | 73p |
| Rhino Prime Set | 70p |
| Boltor Prime Set | 70p |
| Carrier Prime Set | 70p |
| Spira Prime Set | 70p |
| Akjagara Prime Set | 70p |
| Nekros Prime Set | 70p |
| Corinth Prime Set | 68p |
| Hydroid Prime Set | 65p |
| Wukong Prime Set | 65p |
| Aksomati Prime Set | 62p |
| Dual Kamas Prime Set | 61p |
| Vectis Prime Set | 61p |
| Titania Prime Set | 61p |
| Frost Prime Set | 60p |
| Saryn Prime Set | 60p |
| Boar Prime Set | 60p |
| Kogake Prime Set | 60p |
| Ankyros Prime Set | 60p |
| Akstiletto Prime Set | 60p |
| Chroma Prime Set | 60p |
| Gara Prime Set | 60p |
| Nidus Prime Set | 60p |
| Khora Prime Set | 60p |
| Loki Prime Set | 57p |
| Prisma Shade Set | 57p |
| Latron Prime Set | 55p |
| Mag Prime Set | 55p |
| Oberon Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Mirage Prime Set | 55p |
| Octavia Prime Set | 55p |
| Hildryn Prime Set | 55p |
| Wyrm Prime Set | 54p |
| Garuda Prime Set | 51p |
| Bo Prime Set | 50p |
| Tipedo Prime Set | 50p |
| Nova Prime Set | 50p |
| Nezha Prime Set | 50p |
| Phantasma Prime Set | 50p |
| Revenant Prime Set | 48p |
| Tenora Prime Set | 46p |
| Baza Prime Set | 45p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
