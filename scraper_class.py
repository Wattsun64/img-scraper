import os
import urllib.request as req
from selenium import webdriver


class Web_Scraper:
    def open_browser(self):
        self.chrome = webdriver.Chrome("/Users/ecochra/img_scraper/webdrivers/chromedriver")

    def close_browser(self):
        self.chrome.close()

    def get_page_img_elements(self, url = "", css = "img"):
        self.chrome.get(url)

        return self.chrome.find_elements_by_css_selector(css)
        
    def download_img(self, url, path):
        print(url, path)

        return True
    