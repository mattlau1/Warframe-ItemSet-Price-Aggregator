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
**Last Updated:** 2026-02-04 20:29 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 260p |
| Braton Vandal Set | 250p |
| Vauban Prime Set | 130p |
| Arum Spinosa Set | 100p |
| Akstiletto Prime Set | 95p |
| Dual Kamas Prime Set | 80p |
| Hespar Set | 80p |
| Limbo Prime Set | 79p |
| Akbolto Prime Set | 78p |
| Kronen Prime Set | 75p |
| Nyx Prime Set | 75p |
| Rhino Prime Set | 70p |
| Wukong Prime Set | 70p |
| Sporothrix Set | 69p |
| Hydroid Prime Set | 65p |
| Dethcube Prime Set | 65p |
| Chroma Prime Set | 65p |
| Nova Prime Set | 65p |
| Frost Prime Set | 63p |
| Titania Prime Set | 62p |
| Nami Skyla Prime Set | 62p |
| Gara Prime Set | 61p |
| Oberon Prime Set | 60p |
| Boar Prime Set | 60p |
| Boltor Prime Set | 60p |
| Atlas Prime Set | 60p |
| Loki Prime Set | 60p |
| Mirage Prime Set | 60p |
| Nekros Prime Set | 60p |
| Nidus Prime Set | 60p |
| Banshee Prime Set | 59p |
| Afuris Prime Set | 57p |
| Carrier Prime Set | 56p |
| Octavia Prime Set | 56p |
| Mag Prime Set | 55p |
| Tekko Prime Set | 55p |
| Garuda Prime Set | 55p |
| Vectis Prime Set | 53p |
| Wyrm Prime Set | 53p |
| Baruuk Prime Set | 53p |
| Nezha Prime Set | 52p |
| Scourge Prime Set | 52p |
| Valkyr Prime Set | 51p |
| Wisp Prime Set | 51p |
| Saryn Prime Set | 50p |
| Latron Prime Set | 50p |
| Bo Prime Set | 50p |
| Kogake Prime Set | 50p |
| Trinity Prime Set | 50p |
| Ballistica Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
