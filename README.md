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
**Last Updated:** 2026-02-15 08:27 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 260p |
| Lato Vandal Set | 251p |
| Vauban Prime Set | 130p |
| Dual Kamas Prime Set | 105p |
| Xiphos Set | 100p |
| Arum Spinosa Set | 100p |
| Sporothrix Set | 100p |
| Hespar Set | 93p |
| Limbo Prime Set | 80p |
| Afuris Prime Set | 80p |
| Akstiletto Prime Set | 77p |
| Spira Prime Set | 76p |
| Vectis Prime Set | 70p |
| Chroma Prime Set | 70p |
| Titania Prime Set | 68p |
| Wukong Prime Set | 66p |
| Nova Prime Set | 66p |
| Kronen Prime Set | 65p |
| Tekko Prime Set | 65p |
| Nekros Prime Set | 65p |
| Carmine Penta Set | 65p |
| Nidus Prime Set | 64p |
| Oberon Prime Set | 61p |
| Frost Prime Set | 60p |
| Rhino Prime Set | 60p |
| Boar Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Nami Skyla Prime Set | 60p |
| Loki Prime Set | 60p |
| Nyx Prime Set | 60p |
| Corinth Prime Set | 60p |
| Gara Prime Set | 60p |
| Carrier Prime Set | 58p |
| Boltor Prime Set | 55p |
| Mirage Prime Set | 55p |
| Prisma Shade Set | 55p |
| Dethcube Prime Set | 52p |
| Wyrm Prime Set | 51p |
| Garuda Prime Set | 51p |
| Khora Prime Set | 51p |
| Hydroid Prime Set | 50p |
| Saryn Prime Set | 50p |
| Helios Prime Set | 50p |
| Mag Prime Set | 50p |
| Trinity Prime Set | 50p |
| Baza Prime Set | 50p |
| Valkyr Prime Set | 50p |
| Atlas Prime Set | 50p |
| Bonewidow Set | 50p |
| Cortege Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
