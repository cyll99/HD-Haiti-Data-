from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

page_url = "https://data.humdata.org/dataset?q=haiti"
# opens the connection and downloads html page from url
try:
    uClient = requests.get(page_url).text
except:
    print("Connection failed")

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient, "html.parser")


# finds each product from the store page
containers = page_soup.findAll("li", {"class": "list-items dataset-item"})

for container in containers:
    print(container.a.text)
    