from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests
import xml.etree.ElementTree as ET

ocha_link = "https://data.humdata.org/dataset?q=haiti"
amerigeoos_link = "https://data.amerigeoss.org/gl/group/amerigeoss?q=haiti"

class Dataset():
    def __init__(self, title, overview, link, date) :
        self.title = title
        self.overview = overview
        self.link = link
        self.date = date


"""
This class processes data from Ocha website.
"""
class Ocha:
    def __init__(self, link):
        self.link = link
        self.datasets = []
        page_url = self.link + "&page="

        # Scraping five pages
        for i in range(1, 5):
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

                date = container.findAll("div", {"class" : "dataset-dates"})
                date = date[0].text.strip().replace('\n', '').replace("\t", "")

                overview = container.findAll("span", {"class" : "download-counts"})
                overview = overview[0].text.strip().replace('\n', '').replace("\t", "")

                dataset = Dataset(title, overview, link, date)
                self.datasets.append(dataset)


"""
This class processes data from Amerigeoos website.
"""
class Amerigeoos:
    def __init__(self, link):
        
        self.link = link
        self.datasets = []


        # Scraping five pages
        for i in range(1, 5):
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

                    dataset = Dataset(title, overview, link, "No date")
                    self.datasets.append(dataset)
                except:
                    print()
        
a = Amerigeoos(amerigeoos_link)
o = Ocha(ocha_link)

datasets = a.datasets + o.datasets

# Supposons que vous avez une liste 'datasets' contenant les informations des datasets

# Créer un élément racine pour le fichier XML
root = ET.Element("datasets")

# Parcourir les informations des datasets et les ajouter à l'élément racine
for dataset in datasets:
    dataset_element = ET.SubElement(root, "dataset")
    
    title_element = ET.SubElement(dataset_element, "title")
    title_element.text = dataset.title
    
    overview_element = ET.SubElement(dataset_element, "overview")
    overview_element.text = dataset.overview
    
    link_element = ET.SubElement(dataset_element, "link")
    link_element.text = dataset.link
    
    date_element = ET.SubElement(dataset_element, "date")
    date_element.text = dataset.date

# Créer un objet ElementTree avec l'élément racine
tree = ET.ElementTree(root)

# Enregistrer l'arborescence XML dans un fichier
tree.write("datasets.xml", encoding="utf-8", xml_declaration=True)
