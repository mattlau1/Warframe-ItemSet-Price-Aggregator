# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
**Last Updated:** 2026-01-23 09:19 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 302p |
| Lato Vandal Set | 300p |
| Vauban Prime Set | 126p |
| Akstiletto Prime Set | 121p |
| Arum Spinosa Set | 120p |
| Dual Kamas Prime Set | 110p |
| Hespar Set | 90p |
| Spira Prime Set | 85p |
| Akbolto Prime Set | 80p |
| Limbo Prime Set | 80p |
| Tekko Prime Set | 75p |
| Afuris Prime Set | 74p |
| Nekros Prime Set | 73p |
| Aksomati Prime Set | 71p |
| Sporothrix Set | 71p |
| Mirage Prime Set | 71p |
| Corinth Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Wukong Prime Set | 70p |
| Boar Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Kronen Prime Set | 70p |
| Nova Prime Set | 70p |
| Nyx Prime Set | 70p |
| Khora Prime Set | 67p |
| Bo Prime Set | 65p |
| Titania Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Gara Prime Set | 65p |
| Nidus Prime Set | 65p |
| Rhino Prime Set | 64p |
| Frost Prime Set | 63p |
| Latron Prime Set | 62p |
| Carrier Prime Set | 62p |
| Loki Prime Set | 62p |
| Octavia Prime Set | 62p |
| Garuda Prime Set | 62p |
| Saryn Prime Set | 61p |
| Baza Prime Set | 61p |
| Chroma Prime Set | 61p |
| Vectis Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Kogake Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Xiphos Set | 60p |
| Atlas Prime Set | 60p |
| Bonewidow Set | 60p |
| Banshee Prime Set | 60p |
| Morgha Set | 60p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)