from bs4 import BeautifulSoup
import requests

target_website = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(target_website.text, "html.parser")

quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
