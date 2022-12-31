from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

class Amerigeoos:
    def __init__(self):
        
        page_url = "https://data.amerigeoss.org/gl/group/amerigeoss?q=haiti&page="

        self.titles, self.descriptions, self.details = list(), list(), list()


        for i in range(1, 5):

            # opens the connection and downloads html page from url
            try:
                uClient = requests.get(page_url + str(i)).text
            except:
                print("Connection failed")

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(uClient, "html.parser")


            # finds each product from the store page
            containers = page_soup.findAll("li", {"class": "dataset-item"})

            for container in containers:
                link = "https://data.amerigeoss.org"+container.a["href"]
                self.details.append(link)
                self.titles.append(container.a.text)
                self.descriptions.append(container.div.div.text)
        