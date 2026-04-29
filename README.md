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
**Last Updated:** 2026-04-29 17:23 UTC

| Item Set | Median Price |
| :--- | :--- |
| Xiphos Set | 100p |
| Hespar Set | 100p |
| Vectis Prime Set | 96p |
| Kronen Prime Set | 90p |
| Akbolto Prime Set | 85p |
| Afuris Prime Set | 85p |
| Vauban Prime Set | 81p |
| Limbo Prime Set | 80p |
| Nidus Prime Set | 80p |
| Mirage Prime Set | 78p |
| Titania Prime Set | 76p |
| Nekros Prime Set | 76p |
| Hydroid Prime Set | 75p |
| Spira Prime Set | 75p |
| Nami Skyla Prime Set | 75p |
| Chroma Prime Set | 75p |
| Carmine Penta Set | 75p |
| Wukong Prime Set | 74p |
| Carrier Prime Set | 72p |
| Akjagara Prime Set | 72p |
| Rhino Prime Set | 71p |
| Kogake Prime Set | 71p |
| Nyx Prime Set | 71p |
| Garuda Prime Set | 71p |
| Destreza Prime Set | 70p |
| Ballistica Prime Set | 70p |
| Octavia Prime Set | 70p |
| Khora Prime Set | 70p |
| Boar Prime Set | 67p |
| Frost Prime Set | 66p |
| Akstiletto Prime Set | 66p |
| Saryn Prime Set | 65p |
| Ankyros Prime Set | 65p |
| Aksomati Prime Set | 65p |
| Loki Prime Set | 65p |
| Corinth Prime Set | 65p |
| Gara Prime Set | 65p |
| Scourge Prime Set | 65p |
| Sybaris Prime Set | 62p |
| Voruna Prime Set | 61p |
| Latron Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Bonewidow Set | 60p |
| Cortege Set | 60p |
| Banshee Prime Set | 60p |
| Equinox Prime Set | 60p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
