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
**Last Updated:** 2026-02-11 05:25 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 270p |
| Braton Vandal Set | 250p |
| Vauban Prime Set | 126p |
| Hespar Set | 105p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 100p |
| Dual Kamas Prime Set | 97p |
| Sporothrix Set | 95p |
| Limbo Prime Set | 81p |
| Nyx Prime Set | 78p |
| Xiphos Set | 75p |
| Wukong Prime Set | 71p |
| Akjagara Prime Set | 71p |
| Akbolto Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nova Prime Set | 70p |
| Carmine Penta Set | 70p |
| Nidus Prime Set | 70p |
| Titania Prime Set | 69p |
| Nekros Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Rhino Prime Set | 65p |
| Boar Prime Set | 65p |
| Nami Skyla Prime Set | 65p |
| Mirage Prime Set | 65p |
| Dethcube Prime Set | 62p |
| Gara Prime Set | 62p |
| Atlas Prime Set | 61p |
| Octavia Prime Set | 61p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Kogake Prime Set | 60p |
| Kronen Prime Set | 60p |
| Tekko Prime Set | 60p |
| Afuris Prime Set | 60p |
| Cinta Set | 60p |
| Banshee Prime Set | 58p |
| Khora Prime Set | 58p |
| Loki Prime Set | 57p |
| Zephyr Prime Set | 57p |
| Frost Prime Set | 56p |
| Mag Prime Set | 56p |
| Valkyr Prime Set | 56p |
| Carrier Prime Set | 55p |
| Wyrm Prime Set | 55p |
| Latron Prime Set | 53p |
| Garuda Prime Set | 53p |
| Saryn Prime Set | 52p |
| Soma Prime Set | 52p |
| Wisp Prime Set | 52p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
