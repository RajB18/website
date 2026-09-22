# website

## Scrapling

[Scrapling](https://github.com/D4Vinci/Scrapling) is installed as a dependency for web scraping.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
scrapling install  # downloads browser binaries for the fetchers extra
```

### Usage

```bash
python example_scrape.py
```

See `example_scrape.py` for a minimal usage example, and the
[Scrapling docs](https://github.com/D4Vinci/Scrapling) for the full API
(HTTP fetchers, stealthy browser fetching, spiders, etc.).
