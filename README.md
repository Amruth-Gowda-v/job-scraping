# Job Listing Scraper

A beginner-friendly Python web-scraping project that collects job titles and company names from the Real Python demo jobs website and exports the results to a CSV file.

## Features

- Sends an HTTP request to the demo job-listings page
- Parses HTML with BeautifulSoup
- Extracts job titles and company names
- Exports the collected records to `jobs.csv`

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
python -m pip install requests beautifulsoup4
```

## Run

```bash
python main.py
```

Run from the repository directory. The generated `jobs.csv` file is written to the current working directory.

## Data source

The current script uses the Real Python practice page at `https://realpython.github.io/fake-jobs/`. It is a sample/demo source, not a live job-search service.

## Possible next steps

- Add request timeouts and clearer error handling
- Make the source URL configurable
- Add location, job description, and listing URL fields
- Avoid duplicate records when exporting multiple runs
