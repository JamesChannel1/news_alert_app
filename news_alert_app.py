import requests
from bs4 import BeautifulSoup
import sqlite3
import time
import pymsgbox

conn = sqlite3.connect("news_website_content.db")
c = conn.cursor()


c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='webscraped_news'")

if not c.fetchone():
    c.execute('CREATE TABLE webscraped_news (text)')


scraped_content = ""


def func0_stored_in_database():
  c.execute('''SELECT text FROM webscraped_news''')
  result = c.fetchone()
  if result is not None:
    return result[0]
  else:
    return ''

def func1_newly_webscraped():
  # replace 'https://www.EXAMPLE-WEBSITE.com' with the website URL you want to webscrape below 
  response = requests.get('https://www.EXAMPLE-WEBSITE.com')
  soup = BeautifulSoup(response.content, 'html.parser')
  # replace 'div', {'class': 'EXAMPLE-CLASS'} with the class name you want to webscrape below
  scraped_content = soup.find_all('div', {'class': 'EXAMPLE-CLASS'})
  text_list = []
  for item in scraped_content:
      text_list.append(item.text)
  text = "".join(text_list)
  return text

def func2_newly_webscraped_updated_into_database():
  # replace 'https://www.EXAMPLE-WEBSITE.com' with the website URL you want to webscrape below 
  response = requests.get('https://www.EXAMPLE-WEBSITE.com')
  soup = BeautifulSoup(response.content, 'html.parser')
  global scraped_content
  # replace 'div', {'class': 'EXAMPLE-CLASS'} with the class name you want to webscrape below
  scraped_content = soup.find_all('div', {'class': 'EXAMPLE-CLASS'})
  text_list = []
  for item in scraped_content:
      text_list.append(item.text)
  text = "".join(text_list)

  c.execute("INSERT INTO webscraped_news (text) VALUES (?)", (text,))
  conn.commit()


def func3a():
  while True:
    old_content = func0_stored_in_database()
    new_content = func1_newly_webscraped()
    if new_content == old_content:
      print("Content has not changed.")
    else:
      print("Content has changed.")
      pymsgbox.alert("New info on news website")
      func2_newly_webscraped_updated_into_database()
    time.sleep(600)


func3a()
