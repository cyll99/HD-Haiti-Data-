import datetime
from bs4 import BeautifulSoup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests


x = datetime.datetime.now()

date = x.strftime("%A, %B %d %Y")
"""
This class handles the exchange rate of the Hatian Currency
"""
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
        self.USD = containers.h4.text.strip() #US dollar

        other_currencies = []
        containers = containers.findAll("div", {"class": "col-sm-4"})

        for container in containers:
            try:
                other_currencies.append(container.find("div", {"style": "display:inline;"}).text.strip())
            except:
                print()

        self.EUR = other_currencies[0] # Euro currency
        self.PES = other_currencies[1]  #Dominican Peso
        self.CAN = other_currencies[2]  # Canadian dollar


class Weather():
    def __init__(self, city = "Port-au-Prince"):

        # importing requests and json
        CITY = city
        API_KEY = "26548f054308ad111b626fa43cc6399f"
        # base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # City Name CITY = "Hyderabad"
        # API key API_KEY = "Your API Key"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY +  "&units=" + "metric"
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
        # getting data in the json format
            data = response.json()
            lon = data["coord"]["lon"]
            lat = data["coord"]["lat"]

            self.date = date
            try:
                self.city = data["name"]+","+data["sys"]["country"]
                self.coord = f"Lon : {lon},  Lat : {lat}"
                self.weather = data["weather"][0]["description"]
                self.temp_C= data["main"]["temp"]
                self.pressure = data["main"]["pressure"]
                self.humidity = data["main"]["humidity"]
                self.sea_level = data["main"]["sea_level"]
                self.grnd_level = data["main"]["grnd_level"]
                self.visibility = (data["visibility"]) / 1000
                self.wind_speed = data["wind"]["speed"]
                self.icon = "http://openweathermap.org/img/wn/" + data["weather"][0]["icon"] + "@2x.png"
     

            except:
                return


        else:
            # showing the error message
            print("Error in the HTTP request")