from time import time, sleep
from random import randint

from requests import get
from bs4 import BeautifulSoup
from advertising import Advertising


class AdFinder:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}

    def __init__(self, url: str, crawling_time: int | float = 1) -> None:
        self.url: str = url
        self.crawling_time: int = crawling_time * 3600  # Time in hours
        self.advertising = Advertising()

    def _send_request(self):
        # Sends a request to an url and returns the response received from the server

        return get(self.url, headers=self.headers)

    @staticmethod
    def _get_source_code(response):
        # Parses the html codes received from the server response and returns an BeautifulSoup object

        return BeautifulSoup(response.text, "html.parser")

    def _find_ads(self, source_code):
        # This function extracts all new ads from the ads page and returns them in a list

        return self.advertising.find_all_ads(source_code)

    def run(self):
        finish_time = time() + self.crawling_time

        while True:
            response = self._send_request()
            source_code = self._get_source_code(response)
            ads = self._find_ads(source_code)
            for ad in ads:
                print(f'title: {ad.get("title")} \n\n url: {ad.get("url")}')
                print('-' * 200)
            if time() >= finish_time:
                return ads

            interval = randint(20, 40)
            sleep(interval)
