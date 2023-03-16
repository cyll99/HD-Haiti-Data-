from flask import Flask, render_template, request
from amerigeoos import Amerigeoos
from change_weather import Exchange_rate, Weather
from news import *
from ocha import Ocha

#links for each website
ocha_link = "https://data.humdata.org/dataset?q=haiti"
amerigeoos_link = "https://data.amerigeoss.org/gl/group/amerigeoss?q=haiti"





app = Flask(__name__)

@app.route('/datasets',  methods =["GET", "POST"])
def result():
    """
    returns a list of datasets about Haiti
    """
    ocha = Ocha(ocha_link)
    amerigeoos = Amerigeoos(amerigeoos_link)

    #Gathering data
    ocha_data = zip(ocha.titles, ocha.descriptions, ocha.details)
    amerigeoos_data = zip(amerigeoos.titles, amerigeoos.descriptions, amerigeoos.details)


    if request.method == "POST":
        # getting input_key in HTML form
        input_key = request.form.get("search")

        ocha = Ocha(ocha_link + f"+{input_key}")
        amerigeoos = Amerigeoos(amerigeoos_link + f"+{input_key}")

        ocha_data = zip(ocha.titles, ocha.descriptions, ocha.details)
        amerigeoos_data = zip(amerigeoos.titles, amerigeoos.descriptions, amerigeoos.details)


        return render_template("index.html", ocha = ocha_data, amerigeoos = amerigeoos_data)
    return render_template("index.html", ocha = ocha_data, amerigeoos = amerigeoos_data)

@app.route('/news',  methods =["GET", "POST"])
def news():
    """
    return a list of articles from three different web sites
    """
    front_news = HaitiLibre()
    nouvelliste = LeNouvelliste()
    loop = HaitiLoop()

    return render_template("news.html", articles = (front_news.articles + loop.articles + nouvelliste.articles))

@app.route('/weather',  methods =["GET", "POST"])
def weather_info():
    """
    returns the weather of a specific city (Port-au-Prince by default)
    """
    weather = Weather()
    if request.method == "POST":
        # getting input_key in HTML form
        city = request.form.get("search")
        weather = Weather(city)

        return render_template("weather.html", weather = weather)
    return render_template("weather.html", weather = weather)



@app.route('/',  methods =["GET", "POST"])
def home():
    """
    Returns the rate exchange, some articles and datasets for the home page
    """
    exchange_rate = Exchange_rate()
    front_news = HaitiLibre()
    weather = Weather()

    
    return render_template("home.html",  rate = exchange_rate, articles = front_news.articles, weather = weather)

if __name__ == '__main__':
    app.run(debug = True)