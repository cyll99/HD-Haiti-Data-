class Dataset():
    def __init__(self, title, overview, link) :
        self.title = title
        self.overview = overview
        self.link = link


from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

"""
This class processes data from Ocha website.
"""
class Ocha:
    def __init__(self, link):
        self.link = link
        self.datasets = []
        page_url = self.link + "&page="

        # Scraping five pages
        for i in range(1, 3):
            page_url_complete = page_url + str(i)   

            # opens the connection and downloads html page from url
            try:
                uClient = requests.get(page_url_complete).text
            except:
                print("Connection failed")

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(uClient, "html.parser")


            # finds each dataset from the store page
            containers = page_soup.findAll("li", {"class": "list-items dataset-item"})
            
            #Saves details about each dataset to display them
            for container in containers:
                title = container.a.text
                link = "https://data.humdata.org"+container.a["href"]
                info = container.findAll("div", {"class" : "dataset-dates"})
                overview = info[0].text.strip().replace('\n', '').replace("\t", "")
                dataset = Dataset(title, overview, link)
                self.datasets.append(dataset)


"""
This class processes data from Amerigeoos website.
"""
class Amerigeoos:
    def __init__(self, link):
        
        self.link = link
        self.datasets = []


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
                    title = container.a.text
                    overview = container.div.div.text

                    dataset = Dataset(title, overview, link)
                    self.datasets.append(dataset)
                except:
                    print()
        