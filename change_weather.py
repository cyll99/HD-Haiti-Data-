import datetime
from bs4 import BeautifulSoup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A, %B %d %Y"))

class Exchange_rate():
     def __init__(self):

        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US'})

        page_url = "https://www.brh.ht/"

          # opens the connection and downloads html page from url
        try:
            webpage = requests.get(page_url, headers=HEADERS)
        except:
            print("Connection failed")

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        soup = BeautifulSoup(webpage.content, "lxml")

        # finds currencies from home page
        containers = soup.find("div", {"class": "quick_access1"})
        self.USD = containers.h4.text.strip()

        other_currencies = []
        containers = containers.findAll("div", {"class": "col-sm-4"})

        for container in containers:
            try:
                other_currencies.append(container.find("div", {"style": "display:inline;"}).text.strip())
            except:
                print()

        self.EUR = other_currencies[0]
        self.PES = other_currencies[1]
        self.CAN = other_currencies[2]


        # print(self.USD)
        # print(self.EUR)
        # print(self.PES)
        # print(self.CAN)

