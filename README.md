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
**Last Updated:** 2026-02-23 01:45 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 271p |
| Lato Vandal Set | 260p |
| Dual Kamas Prime Set | 120p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 90p |
| Vauban Prime Set | 85p |
| Kronen Prime Set | 81p |
| Sporothrix Set | 81p |
| Hespar Set | 81p |
| Limbo Prime Set | 80p |
| Carmine Penta Set | 80p |
| Afuris Prime Set | 80p |
| Spira Prime Set | 75p |
| Nyx Prime Set | 75p |
| Mirage Prime Set | 75p |
| Nami Skyla Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Wukong Prime Set | 70p |
| Chroma Prime Set | 70p |
| Corinth Prime Set | 70p |
| Nekros Prime Set | 67p |
| Nidus Prime Set | 67p |
| Titania Prime Set | 66p |
| Rhino Prime Set | 65p |
| Oberon Prime Set | 65p |
| Carrier Prime Set | 65p |
| Tekko Prime Set | 65p |
| Banshee Prime Set | 65p |
| Nova Prime Set | 65p |
| Aksomati Prime Set | 62p |
| Octavia Prime Set | 62p |
| Loki Prime Set | 61p |
| Gara Prime Set | 61p |
| Frost Prime Set | 60p |
| Mag Prime Set | 60p |
| Boltor Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Khora Prime Set | 60p |
| Saryn Prime Set | 55p |
| Kogake Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Tipedo Prime Set | 55p |
| Scourge Prime Set | 55p |
| Trinity Prime Set | 51p |
| Equinox Prime Set | 51p |
| Garuda Prime Set | 51p |
| Latron Prime Set | 50p |
| Vectis Prime Set | 50p |
| Ninkondi Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
