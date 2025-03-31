# 📰 Fed News Web Scraper

This Python script scrapes press release articles from the [Federal Reserve's official press release page](https://www.federalreserve.gov/newsevents/pressreleases.htm) using Selenium. It extracts the title, description, and release date of each article and saves the data into a CSV file.

---

## 🚀 Features

- Uses Selenium to automate Chrome browser interaction
- Extracts:
  - Title of the article
  - Main description/paragraph
  - Release date
- Saves the scraped data into a CSV file: `News_release_FED.csv`

---

## 🧰 Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (must match your Chrome version)

### 📦 Python Libraries

Install the required packages:

```bash
pip install selenium
```

---

## 📂 File Structure

```bash
main.py                # Main scraping script
News_release_FED.csv   # Output CSV file with scraped data
```

---

## 🛠️ How It Works

- Launches Chrome using Selenium.
- Navigates to the Federal Reserve press release page.
- Extracts all article links on the page.
- Iterates over each article:
  - Visits the article page.
  - Scrapes the title, release date, and main paragraph.
- Saves all results into a CSV file.

---

## 💡 Notes

- Make sure your ChromeDriver is in your system PATH.
- The script uses `chrome_options.add_experimental_option("detach", True)` so the browser stays open after execution.
- You can modify the sleep intervals for faster or slower execution.

---

## 📈 Example Output

```csv
title,Article,date
"Federal Reserve announces ...","The Federal Reserve Board ...","March 30, 2025"
...
```

---

## 📜 License

MIT License

```vbnet
Copy
Edit
```

Let me know if you want to convert this into an actual file or add CLI arguments for customization!
