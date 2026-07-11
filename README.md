# Brochure Generator

Turn any company's website into a polished, ready-to-share brochure — automatically.

Brochure Generator scrapes a company's site, intelligently selects the most relevant
pages (About, Careers, Products, and more), and uses an OpenAI model to write a concise,
well-structured brochure in Markdown. Perfect for prospective customers, investors, and
recruits who want the essence of a company at a glance.

## Features

- **One command, one brochure** — point it at a homepage and get finished Markdown back.
- **Smart page selection** — an LLM reads the site's links and picks the ones that matter,
  skipping noise like Terms of Service and Privacy pages.
- **Clean, readable output** — brochures come out as Markdown, ready to paste into docs,
  wikis, emails, or static sites.
- **Simple, modular codebase** — scraping, prompts, and LLM orchestration live in small,
  focused modules that are easy to read and extend.

## How It Works

1. **Scrape** — fetch the landing page and collect its links.
2. **Select** — the model reviews the links and returns the ones most useful for a
   brochure (About, Company, Careers, and similar).
3. **Assemble** — the landing page and top selected pages are combined into a single
   context.
4. **Generate** — the model turns that context into a short, engaging brochure highlighting
   the company's culture, customers, and opportunities.

## Project Structure

```
brochure/
├── scraper.py    # Fetches page content and links (Scraper dataclass)
├── prompts.py    # System and user prompts for link selection and brochure writing
└── llm.py        # LLM class that orchestrates the full pipeline
```

## Getting Started

### Prerequisites

- Python 3.9+
- An OpenAI API key

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the generator from the project root:

```bash
PYTHONPATH=. python3 -m brochure.llm
```

Or use it directly in your own code:

```python
from brochure.llm import LLM

llm = LLM()
brochure = llm.generate_brochure("HuggingFace", "https://huggingface.co")
print(brochure)
```

`generate_brochure(company_name, url)` returns the finished brochure as a Markdown string —
print it, save it to a file, or render it anywhere Markdown is supported.

## Built With

- [OpenAI](https://platform.openai.com/) — brochure generation
- [Requests](https://requests.readthedocs.io/) — HTTP fetching
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment configuration
