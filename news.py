from bs4 import BeautifulSoup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

class Article():
    def __init__(self, image, title, overview, link) :
        self.image = image
        self.title = title
        self.overview = overview
        self.link = link


class HaitiLibre():
    def __init__(self):

        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US'})
        
        page_url = "https://www.haitilibre.com/en/"

          # opens the connection and downloads html page from url
        try:
            webpage = requests.get(page_url, headers=HEADERS)
        except:
            print("Connection failed")

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        soup = BeautifulSoup(webpage.content, "lxml")

        # finds news from home page
        containers = soup.findAll("table", {"width": "100%"})
        self.articles = []
        for container in containers:
            try:
                image = "https://www.haitilibre.com" + container.find("img")["src"].strip()
                title = container.find("img")["alt"]
                overview = container.findAll("td", {"class": "text"})[1].text.strip()
                link = "https://www.haitilibre.com" + container.findAll("td", {"class": "text"})[2].a["href"]

                article = Article(image, title, overview, link)
                self.articles.append(article)
            except:
                continue



class LeNouvelliste():
    def __init__(self):

        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US'})
        
        page_url = "https://www.lenouvelliste.com/"

                  # opens the connection and downloads html page from url
        try:
            webpage = requests.get(page_url, headers=HEADERS)
        except:
            print("Connection failed")

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        soup = BeautifulSoup(webpage.content, "lxml")

                # finds news from home page
        containers = soup.findAll("div", {"class": "lnv-featured-article-sm"})
        self.articles = []
        for container in containers:
            try:
                image = container.find("img")["src"].strip()
                title = container.find("h1").strip()
                overview = container.find("p").strip()
                link = "https://www.lenouvelliste.com" + container.find("a")["href"]

                print(f"image = {image}")
                print(f"title = {title}")
                print(f"overview = {overview}")
                print(f"link = {link}")


                article = Article(image, title, overview, link)
                self.articles.append(article)
            except:
                continue

