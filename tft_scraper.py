from functools import reduce

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from tft import TFT


class TFTScraper:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 5)
        self.url = "https://www.eii.ulpgc.es/es/informacionacademica/tft/ofertatft"
        self.scraped_pages = 0
        self.scraped_results = 0
        self.errors = 0
        self.total_results: int | None = None

    def scrape_tfts(self) -> list[TFT]:
        self.driver.get(self.url)
        self.total_results = self._get_total_results()
        tfts = []
        while current_page_tfts := self._get_current_page_tfts():
            tfts.extend(current_page_tfts)
            self._go_to_next_page()
        self.driver.close()
        return tfts

    def _get_total_results(self):
        results_count_footer_selector = "//div[@id='page-main-content']//footer[contains(text(), 'Mostrando')]"
        results_count_footer = self.driver.find_element(By.XPATH, results_count_footer_selector)
        return int(results_count_footer.text.split("de ")[1])

    def _go_to_next_page(self):
        self.scraped_pages += 1
        self.driver.get(self._page_url)

    def _get_current_page_tfts(self) -> list[TFT]:
        try:
            tft_list = self.driver.find_element(By.ID, "accordion-ptft")
            tft_items = tft_list.find_elements(By.CSS_SELECTOR, "div.item div.panel")
            return [self._extract_tft_data(tft_item) for tft_item in tft_items if tft_item is not None]
        except NoSuchElementException:
            return []

    def _extract_tft_data(self, tft_element: WebElement) -> TFT | None:
        try:
            body_paragraphs = tft_element.find_elements(By.CSS_SELECTOR, ".panel-body p")
            description = reduce(lambda acc, p: f"{acc}{p.get_attribute('innerHTML')}\n", body_paragraphs, "\n")
            tft = TFT(
                title=tft_element.find_element(By.CSS_SELECTOR, '.panel-title a').text,
                description=description,
                contact=tft_element.find_element(By.XPATH, ".//div[span[contains(text(), 'Contacto:')]]")
                .get_attribute("innerHTML")
                .split("</span>")[1],
                source=self._page_url
            )
            self.scraped_results += 1
            return tft
        except NoSuchElementException:
            self.errors += 1
            return

    @property
    def _page_url(self):
        return self.url + f"?field_tft_contacto_value=&page={self.scraped_pages}"

    @property
    def scraping_outcome(self):
        return (f"Scraped {self.scraped_pages} pages and {self.scraped_results} results out "
                f"of {self.total_results or '?'} total results. There were {self.errors} errors.")
