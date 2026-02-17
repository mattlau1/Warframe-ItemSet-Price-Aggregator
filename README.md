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
**Last Updated:** 2026-02-17 01:43 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 201p |
| Braton Vandal Set | 200p |
| Vauban Prime Set | 130p |
| Dual Kamas Prime Set | 100p |
| Hespar Set | 100p |
| Sporothrix Set | 81p |
| Limbo Prime Set | 80p |
| Arum Spinosa Set | 80p |
| Akstiletto Prime Set | 73p |
| Nova Prime Set | 66p |
| Wukong Prime Set | 65p |
| Nami Skyla Prime Set | 65p |
| Kronen Prime Set | 63p |
| Mag Prime Set | 61p |
| Rhino Prime Set | 60p |
| Carrier Prime Set | 60p |
| Titania Prime Set | 60p |
| Chroma Prime Set | 60p |
| Nekros Prime Set | 60p |
| Morgha Set | 60p |
| Nyx Prime Set | 57p |
| Carmine Penta Set | 57p |
| Frost Prime Set | 56p |
| Octavia Prime Set | 56p |
| Hydroid Prime Set | 55p |
| Oberon Prime Set | 55p |
| Kogake Prime Set | 55p |
| Loki Prime Set | 55p |
| Mirage Prime Set | 55p |
| Gara Prime Set | 55p |
| Nidus Prime Set | 55p |
| Boltor Prime Set | 53p |
| Equinox Prime Set | 53p |
| Tekko Prime Set | 52p |
| Zephyr Prime Set | 52p |
| Akjagara Prime Set | 51p |
| Saryn Prime Set | 50p |
| Vectis Prime Set | 50p |
| Boar Prime Set | 50p |
| Dethcube Prime Set | 50p |
| Aksomati Prime Set | 50p |
| Hikou Prime Set | 50p |
| Valkyr Prime Set | 50p |
| Atlas Prime Set | 50p |
| Bonewidow Set | 50p |
| Cortege Set | 50p |
| Corinth Prime Set | 50p |
| Garuda Prime Set | 50p |
| Khora Prime Set | 50p |
| Bo Prime Set | 48p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
