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
**Last Updated:** 2026-01-02 23:09 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 256p |
| Lato Vandal Set | 255p |
| Akstiletto Prime Set | 116p |
| Vauban Prime Set | 116p |
| Arum Spinosa Set | 100p |
| Spira Prime Set | 96p |
| Hespar Set | 95p |
| Nami Skyla Prime Set | 92p |
| Dual Kamas Prime Set | 87p |
| Limbo Prime Set | 80p |
| Sporothrix Set | 80p |
| Nekros Prime Set | 76p |
| Saryn Prime Set | 72p |
| Akjagara Prime Set | 71p |
| Valkyr Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nova Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Carrier Prime Set | 65p |
| Aksomati Prime Set | 65p |
| Nikana Prime Set | 65p |
| Nyx Prime Set | 65p |
| Carmine Penta Set | 65p |
| Gyre Prime Set | 65p |
| Wukong Prime Set | 63p |
| Titania Prime Set | 63p |
| Kronen Prime Set | 63p |
| Loki Prime Set | 62p |
| Vectis Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Akbolto Prime Set | 60p |
| Xiphos Set | 60p |
| Atlas Prime Set | 60p |
| Nidus Prime Set | 60p |
| Scourge Prime Set | 60p |
| Garuda Prime Set | 60p |
| Khora Prime Set | 60p |
| Mag Prime Set | 59p |
| Oberon Prime Set | 56p |
| Frost Prime Set | 55p |
| Trinity Prime Set | 55p |
| Rhino Prime Set | 52p |
| Tekko Prime Set | 52p |
| Morgha Set | 52p |
| Phantasma Prime Set | 52p |
| Chroma Prime Set | 51p |
| Gara Prime Set | 51p |
| Sicarus Prime Set | 50p |
| Ballistica Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)