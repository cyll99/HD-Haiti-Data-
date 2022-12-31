from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests


class Ocha:
    def __init__(self):
        
        page_url = "https://data.humdata.org/dataset?q=haiti&page="
        self.titles, self.descriptions, self.details = list(), list(), list()


        for i in range(1, 5):
            page_url = page_url + str(i)
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
                self.titles.append(container.a.text)
                link = "https://data.humdata.org"+container.a["href"]
                self.details.append(link)
                info = container.findAll("div", {"class" : "dataset-dates"})
                self.descriptions.append(info[0].text.strip().replace('\n', '').replace("\t", ""))
            