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
**Last Updated:** 2026-01-18 00:54 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 316p |
| Braton Vandal Set | 307p |
| Vauban Prime Set | 115p |
| Arum Spinosa Set | 110p |
| Akstiletto Prime Set | 95p |
| Hespar Set | 95p |
| Limbo Prime Set | 82p |
| Aksomati Prime Set | 80p |
| Spira Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Afuris Prime Set | 80p |
| Nekros Prime Set | 72p |
| Dual Kamas Prime Set | 71p |
| Dethcube Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Saryn Prime Set | 70p |
| Wukong Prime Set | 70p |
| Boar Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Kronen Prime Set | 70p |
| Tekko Prime Set | 70p |
| Nyx Prime Set | 70p |
| Carmine Penta Set | 68p |
| Garuda Prime Set | 68p |
| Titania Prime Set | 67p |
| Mirage Prime Set | 67p |
| Nidus Prime Set | 67p |
| Kogake Prime Set | 65p |
| Carrier Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Atlas Prime Set | 65p |
| Nova Prime Set | 65p |
| Corinth Prime Set | 65p |
| Gara Prime Set | 65p |
| Scourge Prime Set | 65p |
| Khora Prime Set | 65p |
| Frost Prime Set | 61p |
| Rhino Prime Set | 61p |
| Venka Prime Set | 60p |
| Baza Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Nikana Prime Set | 60p |
| Sporothrix Set | 60p |
| Chroma Prime Set | 60p |
| Loki Prime Set | 60p |
| Oberon Prime Set | 58p |
| Ballistica Prime Set | 58p |
| Mag Prime Set | 55p |
| Ankyros Prime Set | 55p |
| Trinity Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)