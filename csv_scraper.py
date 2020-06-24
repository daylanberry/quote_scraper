from bs4 import BeautifulSoup
import requests
from random import choice
from csv import DictWriter

base = 'http://quotes.toscrape.com'

def scrape_quotes():
  all_quotes = []
  url = '/page/1'
  while url:

    res = requests.get(f"{base}{url}").text
    print(f"scraping {base}{url}")
    soup = BeautifulSoup(res, 'html.parser')
    quotes = soup.find_all(class_='quote')

    for quote in quotes:
      quote_obj = {
          "text": quote.find(class_='text').get_text(),
          "author": quote.find(class_='author').get_text(),
          'bio-link': quote.find('a')['href']
      }
      all_quotes.append(quote_obj)

    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None

  return all_quotes

quotes = scrape_quotes()

def write_quotes(quotes):
  with open('quotes.csv', 'w') as file:
    headers = ['text', 'author', 'bio-link']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()

    for quote in quotes:
      csv_writer.writerow(quote)

write_quotes(quotes)