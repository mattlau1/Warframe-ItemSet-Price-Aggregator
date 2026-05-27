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
**Last Updated:** 2026-05-27 15:23 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 105p |
| Hespar Set | 100p |
| Akbolto Prime Set | 93p |
| Afuris Prime Set | 90p |
| Nami Skyla Prime Set | 86p |
| Kronen Prime Set | 85p |
| Vauban Prime Set | 85p |
| Limbo Prime Set | 81p |
| Hydroid Prime Set | 80p |
| Carrier Prime Set | 80p |
| Spira Prime Set | 80p |
| Nekros Prime Set | 80p |
| Wukong Prime Set | 76p |
| Nidus Prime Set | 76p |
| Titania Prime Set | 75p |
| Corinth Prime Set | 75p |
| Kogake Prime Set | 72p |
| Chroma Prime Set | 71p |
| Mirage Prime Set | 71p |
| Octavia Prime Set | 71p |
| Bo Prime Set | 70p |
| Boar Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Garuda Prime Set | 70p |
| Khora Prime Set | 70p |
| Scourge Prime Set | 67p |
| Frost Prime Set | 66p |
| Oberon Prime Set | 66p |
| Akstiletto Prime Set | 66p |
| Loki Prime Set | 66p |
| Saryn Prime Set | 65p |
| Latron Prime Set | 65p |
| Mag Prime Set | 65p |
| Tipedo Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Gara Prime Set | 65p |
| Cinta Set | 65p |
| Ballistica Prime Set | 61p |
| Zephyr Prime Set | 61p |
| Wisp Prime Set | 61p |
| Ninkondi Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Xiphos Set | 60p |
| Bonewidow Set | 60p |
| Nova Prime Set | 60p |
| Equinox Prime Set | 60p |
| Mesa Prime Set | 60p |
| Tenora Prime Set | 60p |

*... (see out.txt for full list of 237 items)*

[//]: # (PRICE_END)
