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
**Last Updated:** 2026-05-26 07:40 UTC

| Item Set | Median Price |
| :--- | :--- |
| Xiphos Set | 120p |
| Hespar Set | 110p |
| Vectis Prime Set | 100p |
| Kronen Prime Set | 95p |
| Vauban Prime Set | 92p |
| Hydroid Prime Set | 90p |
| Akbolto Prime Set | 90p |
| Nami Skyla Prime Set | 90p |
| Afuris Prime Set | 90p |
| Carrier Prime Set | 85p |
| Limbo Prime Set | 85p |
| Wukong Prime Set | 82p |
| Nekros Prime Set | 80p |
| Titania Prime Set | 78p |
| Nidus Prime Set | 76p |
| Kogake Prime Set | 75p |
| Ballistica Prime Set | 75p |
| Chroma Prime Set | 75p |
| Mirage Prime Set | 75p |
| Corinth Prime Set | 75p |
| Garuda Prime Set | 75p |
| Khora Prime Set | 75p |
| Frost Prime Set | 70p |
| Oberon Prime Set | 70p |
| Spira Prime Set | 70p |
| Octavia Prime Set | 70p |
| Gara Prime Set | 70p |
| Scourge Prime Set | 70p |
| Saryn Prime Set | 68p |
| Zephyr Prime Set | 67p |
| Latron Prime Set | 65p |
| Mag Prime Set | 65p |
| Bo Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Banshee Prime Set | 65p |
| Loki Prime Set | 65p |
| Equinox Prime Set | 65p |
| Prisma Shade Set | 65p |
| Phantasma Prime Set | 63p |
| Aksomati Prime Set | 61p |
| Valkyr Prime Set | 61p |
| Cinta Set | 61p |
| Boar Prime Set | 60p |
| Baza Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Glaive Prime Set | 60p |
| Tipedo Prime Set | 60p |
| Nova Prime Set | 60p |
| Carmine Penta Set | 60p |
| Harrow Prime Set | 60p |

*... (see out.txt for full list of 238 items)*

[//]: # (PRICE_END)
