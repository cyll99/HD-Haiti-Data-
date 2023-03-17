from flask import Flask, render_template, request
from change_weather import Exchange_rate, Weather
from news import *
from dataset import Ocha, Amerigeoos

#links for each website
ocha_link = "https://data.humdata.org/dataset?q=haiti"
amerigeoos_link = "https://data.amerigeoss.org/gl/group/amerigeoss?q=haiti"


ocha = Ocha(ocha_link)
amerigeoos = Amerigeoos(amerigeoos_link)


app = Flask(__name__)

@app.route('/datasets',  methods =["GET", "POST"])
def result():
    """
    returns a list of datasets about Haiti
    """
  

    ocha = Ocha(ocha_link)
    amerigeoos = Amerigeoos(amerigeoos_link)

    if request.method == "POST":
        # getting input_key in HTML form
        input_key = request.form.get("search")

        ocha = Ocha(ocha_link + f"+{input_key}")
        amerigeoos = Amerigeoos(amerigeoos_link + f"+{input_key}")

        return render_template("index.html", ochas = ocha.datasets, ameri = amerigeoos.datasets)
    return render_template("index.html", ochas = ocha.datasets, ameri = amerigeoos.datasets)


@app.route('/news',  methods =["GET", "POST"])
def news():
    """
    return a list of articles from three different web sites
    """
    front_news = HaitiLibre()
    nouvelliste = LeNouvelliste()
    # loop = HaitiLoop()

    return render_template("news.html", articles = (front_news.articles + nouvelliste.articles))

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

    # exchange_rate = Exchange_rate()
    front_news = HaitiLibre()
    weather = Weather()

    if request.method == "POST":
        # getting input_key in HTML form
        city = request.form.get("search")
        weather = Weather(city)

        return render_template("home.html", ameri = amerigeoos.datasets, articles = front_news.articles, weather = weather)
    
    return render_template("home.html", ameri = amerigeoos.datasets, articles = front_news.articles, weather = weather)

if __name__ == '__main__':
    app.run(debug = True)