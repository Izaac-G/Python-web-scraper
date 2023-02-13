from bs4 import BeautifulSoup
import requests

dr_website = requests.get("https://www.darkreading.com")
tp_website = requests.get("https://threatpost.com")
kob_website = requests.get("https://krebsonsecurity.com")
ns_website = requests.get("https://nakedsecurity.sophos.com")


soup = BeautifulSoup(dr_website.text, "html.parser")
dr_main_headlines = soup.findAll("a", attrs={"class":"spotlight-left-title"})
dr_side_headlines = soup.findAll("a", attrs={"class":"article-title"})
print("\n" + "Here are the top headlines for today from www.darkreading.com:")
for headline in dr_main_headlines:
    print("\t-" + headline.text)
for headline in dr_side_headlines:
    print("\t-" + headline.text)

soup = BeautifulSoup(tp_website.text, "html.parser")
tp_headlines = soup.findAll("h2", attrs={"class":"c-card__title"})
print("\n" + "Here are the top headlines for today from www.threatpost.com:")
for headline in tp_headlines[:5]:
    print("\t-" + headline.text)

soup = BeautifulSoup(ns_website.text, "html.parser")
ns_slide_headlines = soup.findAll("h2", attrs={"class":"slide-title"})
ns_card_headlines = soup.findAll("h3", attrs={"class":"card-title"})
print("\n" + "Here are a few of the most recent blogposts from nakedsecurity.sophos.com")

for headline in ns_slide_headlines:
    print("\t-" + headline.text)
for headline in ns_card_headlines[:3]:
    print("\t-" + headline.text)

soup = BeautifulSoup(kob_website.text, "html.parser")
kob_headlines = soup.findAll("h2", attrs={"class":"entry-title"})
print("\n" + "Here are a few of the most recent blogposts from krebsonsecurity.com")
for headline in kob_headlines[:4]:
    print("\t-" + headline.text.strip())


