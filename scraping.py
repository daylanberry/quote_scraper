from bs4 import BeautifulSoup
import requests
from random import choice


def start_game(quotes):
  quote = choice(quotes)
  remaining = 4
  print ("Heres a quote: ''")
  print(quote['text'])
  print(quote['author'])
  guess = ''

  while  guess.lower() != quote['author'].lower() and remaining > 0:
    guess = input(f"Who said this quote? Guesses Remaing: {remaining} ")
    remaining -=1
    if guess.lower() == quote['author'].lower():
      print('You got it right!')
      break
    if remaining == 3:
      print(f"{base}{quote['bio-link']}")
      res = requests.get(f"{base}{quote['bio-link']}").text
      soup = BeautifulSoup(res, 'html.parser')

      birth_date = soup.find(class_='author-born-date').get_text()
      birth_location = soup.find(class_='author-born-location').get_text()
      print(f"Heres a hint: The author was born on {birth_date} {birth_location}")
    elif remaining == 2:
      print(f"Authors first name starts with: {quote['author'][0]}")
    elif remaining == 1:
      last = quote['author'].split(' ')
      first_last = last[1][0]
      print(f"The last name starts with: {first_last}")
    else:
      print(f"You ran out! The answer was: {quote['author']}")

  again = ' '

  while again not in ('y', 'yes', 'n', 'no'):
    again = input('would you like to play again? (y/n)?')


  if again.lower() in ('yes', 'y'):
    return start_game(quotes)
  else:
    print('ok goodbye')


quotes = scrape_quotes()

start_game(quotes)
