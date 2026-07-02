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
**Last Updated:** 2026-07-02 02:43 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 120p |
| Vectis Prime Set | 106p |
| Hespar Set | 95p |
| Destreza Prime Set | 91p |
| Vauban Prime Set | 86p |
| Spira Prime Set | 85p |
| Limbo Prime Set | 80p |
| Nekros Prime Set | 80p |
| Carmine Penta Set | 80p |
| Nidus Prime Set | 80p |
| Afuris Prime Set | 80p |
| Akstiletto Prime Set | 75p |
| Kronen Prime Set | 75p |
| Hydroid Prime Set | 71p |
| Saryn Prime Set | 70p |
| Carrier Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Corinth Prime Set | 66p |
| Frost Prime Set | 65p |
| Oberon Prime Set | 65p |
| Boar Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Loki Prime Set | 65p |
| Garuda Prime Set | 65p |
| Khora Prime Set | 65p |
| Banshee Prime Set | 62p |
| Chroma Prime Set | 61p |
| Wukong Prime Set | 60p |
| Bo Prime Set | 60p |
| Titania Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Xiphos Set | 60p |
| Tekko Prime Set | 60p |
| Rubico Prime Set | 60p |
| Mirage Prime Set | 60p |
| Octavia Prime Set | 60p |
| Nautilus Set | 60p |
| Scourge Prime Set | 60p |
| Styanax Prime Set | 60p |
| Afentis Prime Set | 60p |
| Dual Kamas Prime Set | 55p |
| Mag Prime Set | 55p |
| Kogake Prime Set | 55p |
| Aksomati Prime Set | 55p |
| Panthera Prime Set | 55p |
| Akjagara Prime Set | 55p |
| Athodai Set | 55p |
| Gara Prime Set | 55p |
| Sybaris Prime Set | 54p |
| Glaive Prime Set | 53p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
