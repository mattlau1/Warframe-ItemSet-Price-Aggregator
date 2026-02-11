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
**Last Updated:** 2026-02-11 08:42 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 275p |
| Braton Vandal Set | 260p |
| Vauban Prime Set | 130p |
| Hespar Set | 105p |
| Dual Kamas Prime Set | 100p |
| Akstiletto Prime Set | 100p |
| Arum Spinosa Set | 100p |
| Sporothrix Set | 82p |
| Limbo Prime Set | 75p |
| Wukong Prime Set | 73p |
| Nyx Prime Set | 73p |
| Akbolto Prime Set | 70p |
| Chroma Prime Set | 70p |
| Nova Prime Set | 70p |
| Mirage Prime Set | 68p |
| Rhino Prime Set | 67p |
| Nekros Prime Set | 66p |
| Boar Prime Set | 65p |
| Titania Prime Set | 65p |
| Nami Skyla Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Loki Prime Set | 63p |
| Frost Prime Set | 62p |
| Kronen Prime Set | 62p |
| Gara Prime Set | 62p |
| Hydroid Prime Set | 61p |
| Atlas Prime Set | 61p |
| Vectis Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Trinity Prime Set | 60p |
| Carrier Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Tekko Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Nidus Prime Set | 60p |
| Afuris Prime Set | 60p |
| Cinta Set | 59p |
| Khora Prime Set | 58p |
| Saryn Prime Set | 56p |
| Mag Prime Set | 56p |
| Banshee Prime Set | 56p |
| Wyrm Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Bonewidow Set | 55p |
| Cortege Set | 55p |
| Carmine Penta Set | 55p |
| Baza Prime Set | 53p |
| Garuda Prime Set | 52p |
| Latron Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)
