## Steam Specials Scraper

This Python script scrapes the latest discounted games from the [Steam Specials](https://store.steampowered.com/search/?specials=1&os=win) page and saves the results to a text file. It displays the title, original price, final price, discount, and a link for each game directly in the terminal with colorized output.

---

**Features**

- Fetches live data from Steam's specials page
- Parses and extracts game titles, prices, discounts, and links
- Colorful terminal output for better readability
- Saves all results to `games_data.txt` with a timestamp
- Graceful error handling for network issues

---

**Requirements**

- Python 3.8+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [colorama](https://pypi.org/project/colorama/)

Install dependencies with:

```bash
pip install requests beautifulsoup4 colorama
```

---

**Usage**

```bash
python scrape.py
```

- The script will print the scraped results to the console.
- Output is also saved to `games_data.txt` in the current directory.

---

**Sample Output**

```
Scraped at: 2025-05-30 17:34:00
------------------------------------------------------------
Title: Game Title
Original Price: $19.99
Final Price: $9.99
Discount: -50%
Link: https://store.steampowered.com/app/xxxxxx
------------------------------------------------------------
Total games found: 20
Data has been saved to 'games_data.txt'.
Script by Adib - www.adib23704.com
```

---

**Customization**

- You can modify the `url` variable in the script to target other Steam search filters.
- The output file and formatting can be adjusted as needed.

---

**Author**

Script by Adib  
www.adib23704.com

---

**License**

This project is licensed under the MIT License.

---

**Disclaimer**

This script is for educational purposes only. Use responsibly and respect Steam's terms of service.