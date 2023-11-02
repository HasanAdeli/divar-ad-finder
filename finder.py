import requests
from bs4 import BeautifulSoup
from advertising import Advertising


class AdFinder:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}

    def __init__(self, url: str) -> None:
        self.url: str = url
        self.advertising = Advertising()

    def send_request(self):
        # Sends a request to a link and returns the response received from the server

        return requests.get(self.url, headers=self.headers)

    @staticmethod
    def get_source_code(response):
        # Parses the html codes received from the server response and returns an BeautifulSoup object

        return BeautifulSoup(response.text, "html.parser")

    def find_ads(self, source_code):
        # This function extracts all new ads from the ads page and returns them in a list

        return self.advertising.find_all_ads(source_code)

    def run(self):
        response = self.send_request()
        source_code = self.get_source_code(response)
        ads = self.find_ads(source_code)
        return ads
