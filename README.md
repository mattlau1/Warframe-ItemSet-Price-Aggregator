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
**Last Updated:** 2026-03-02 08:37 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 230p |
| Lato Vandal Set | 211p |
| Dual Kamas Prime Set | 100p |
| Hespar Set | 95p |
| Akbolto Prime Set | 80p |
| Kronen Prime Set | 80p |
| Vauban Prime Set | 80p |
| Titania Prime Set | 75p |
| Akstiletto Prime Set | 75p |
| Mirage Prime Set | 75p |
| Limbo Prime Set | 70p |
| Sporothrix Set | 70p |
| Chroma Prime Set | 70p |
| Nova Prime Set | 70p |
| Nekros Prime Set | 70p |
| Nidus Prime Set | 70p |
| Arum Spinosa Set | 66p |
| Hydroid Prime Set | 65p |
| Spira Prime Set | 65p |
| Rhino Prime Set | 61p |
| Frost Prime Set | 60p |
| Vectis Prime Set | 60p |
| Wukong Prime Set | 60p |
| Ankyros Prime Set | 60p |
| Trinity Prime Set | 60p |
| Carrier Prime Set | 60p |
| Banshee Prime Set | 60p |
| Nyx Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Afuris Prime Set | 60p |
| Valkyr Prime Set | 56p |
| Saryn Prime Set | 55p |
| Mag Prime Set | 55p |
| Oberon Prime Set | 55p |
| Bo Prime Set | 55p |
| Boar Prime Set | 55p |
| Corinth Prime Set | 55p |
| Octavia Prime Set | 55p |
| Khora Prime Set | 55p |
| Wisp Prime Set | 55p |
| Grendel Prime Set | 55p |
| Wyrm Prime Set | 54p |
| Equinox Prime Set | 53p |
| Tipedo Prime Set | 52p |
| Tenora Prime Set | 52p |
| Nautilus Set | 52p |
| Akarius Prime Set | 52p |
| Destreza Prime Set | 50p |
| Helios Prime Set | 50p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
