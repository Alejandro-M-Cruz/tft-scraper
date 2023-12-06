from tft import TFT
from tft_scraper import TFTScraper

if __name__ == "__main__":
    scraper = TFTScraper()
    tfts = scraper.scrape_tfts()
    with open(".tfts", "w") as f:
        f.write(TFT.separator.join([repr(tft) for tft in tfts]))
    print(scraper.scraping_outcome)
