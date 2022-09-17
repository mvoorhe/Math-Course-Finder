from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class Scraper():
    def scrapdata(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}/page/1/'
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        qlist = []

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(text)
            qlist.append(text)
        return qlist

quotes = Scraper()
quotes.scrapdata('life')



