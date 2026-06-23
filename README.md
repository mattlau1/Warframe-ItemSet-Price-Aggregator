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
**Last Updated:** 2026-06-23 10:58 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 135p |
| Vectis Prime Set | 120p |
| Destreza Prime Set | 90p |
| Vauban Prime Set | 85p |
| Afentis Prime Set | 82p |
| Nidus Prime Set | 81p |
| Afuris Prime Set | 81p |
| Spira Prime Set | 80p |
| Kronen Prime Set | 80p |
| Akjagara Prime Set | 80p |
| Nekros Prime Set | 80p |
| Styanax Prime Set | 80p |
| Hydroid Prime Set | 75p |
| Garuda Prime Set | 75p |
| Hespar Set | 75p |
| Khora Prime Set | 71p |
| Carrier Prime Set | 70p |
| Limbo Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Mirage Prime Set | 70p |
| Gara Prime Set | 67p |
| Frost Prime Set | 66p |
| Titania Prime Set | 66p |
| Wyrm Prime Set | 65p |
| Chroma Prime Set | 65p |
| Banshee Prime Set | 65p |
| Loki Prime Set | 65p |
| Octavia Prime Set | 65p |
| Scourge Prime Set | 64p |
| Sybaris Prime Set | 63p |
| Mag Prime Set | 62p |
| Bo Prime Set | 62p |
| Phantasma Prime Set | 62p |
| Saryn Prime Set | 60p |
| Wukong Prime Set | 60p |
| Oberon Prime Set | 60p |
| Boar Prime Set | 60p |
| Akstiletto Prime Set | 60p |
| Panthera Prime Set | 60p |
| Xiphos Set | 60p |
| Bonewidow Set | 60p |
| Corinth Prime Set | 60p |
| Aksomati Prime Set | 57p |
| Volt Prime Set | 56p |
| Akarius Prime Set | 56p |
| Latron Prime Set | 55p |
| Dethcube Prime Set | 55p |
| Baza Prime Set | 55p |
| Glaive Prime Set | 55p |
| Valkyr Prime Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
