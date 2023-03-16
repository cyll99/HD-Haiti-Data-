from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests


"""
This class processes data from Amerigeoos website.
"""
class Amerigeoos:
    def __init__(self, link):
        
        self.link = link

        self.titles, self.descriptions, self.details = list(), list(), list()

        # Scraping five pages
        for i in range(1, 3):
            page_url = self.link + "&page=" + str(i) 
            
            # opens the connection and downloads html page from url
            try:
                uClient = requests.get(page_url).text
            except:
                print("Connection failed")

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(uClient, "html.parser")


            # finds each dataset from the store page
            containers = page_soup.findAll("li", {"class": "dataset-item"})
            #Saves details about each dataset to display them
            for container in containers:
                try:
                    link = "https://data.amerigeoss.org"+container.a["href"]
                    self.details.append(link)
                    self.titles.append(container.a.text)
                    self.descriptions.append(container.div.div.text)
                except:
                    print()
        