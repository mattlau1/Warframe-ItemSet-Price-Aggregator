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
**Last Updated:** 2026-02-13 08:37 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 260p |
| Braton Vandal Set | 250p |
| Vauban Prime Set | 126p |
| Akstiletto Prime Set | 103p |
| Hespar Set | 100p |
| Dual Kamas Prime Set | 95p |
| Sporothrix Set | 90p |
| Arum Spinosa Set | 80p |
| Afuris Prime Set | 79p |
| Limbo Prime Set | 76p |
| Vectis Prime Set | 72p |
| Aksomati Prime Set | 69p |
| Nova Prime Set | 68p |
| Kronen Prime Set | 67p |
| Nekros Prime Set | 66p |
| Corinth Prime Set | 66p |
| Hydroid Prime Set | 65p |
| Titania Prime Set | 65p |
| Chroma Prime Set | 65p |
| Akjagara Prime Set | 65p |
| Nidus Prime Set | 61p |
| Frost Prime Set | 60p |
| Oberon Prime Set | 60p |
| Carrier Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Spira Prime Set | 60p |
| Loki Prime Set | 60p |
| Nyx Prime Set | 60p |
| Mirage Prime Set | 60p |
| Akbolto Prime Set | 58p |
| Boar Prime Set | 56p |
| Ankyros Prime Set | 56p |
| Banshee Prime Set | 56p |
| Latron Prime Set | 55p |
| Wukong Prime Set | 55p |
| Mag Prime Set | 55p |
| Bo Prime Set | 55p |
| Nami Skyla Prime Set | 55p |
| Nezha Prime Set | 55p |
| Carmine Penta Set | 55p |
| Trinity Prime Set | 53p |
| Baza Prime Set | 53p |
| Khora Prime Set | 53p |
| Saryn Prime Set | 51p |
| Destreza Prime Set | 50p |
| Kogake Prime Set | 50p |
| Ballistica Prime Set | 50p |
| Valkyr Prime Set | 50p |
| Octavia Prime Set | 50p |

*... (see out.txt for full list of 234 items)*

[//]: # (PRICE_END)
