from bs4 import BeautifulSoup
import requests

target_website = input("What is the URL of the target website you would like to scrape?\n")
target_request = requests.get(target_website)
soup = BeautifulSoup(target_request.text, "html.parser")

item_flag = input("What is the tag of the item you would like to parse for? (ex. span, small, p)\n")
item_class = input("What is the class of the item you would like to scrape?(ex. text, author, content)\n")

target_items = soup.findAll(item_flag, attrs = {"class":item_class})

print(f"The items with class: {item_class} and flag: {item_flag} from URL: {target_website} are as follows: \n")
for item in target_items:
    print(item.text + "\n")
