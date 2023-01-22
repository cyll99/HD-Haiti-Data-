from flask import Flask, render_template, request
from amerigeoos import Amerigeoos
from change_weather import Exchange_rate
from news import HaitiLibre
from ocha import Ocha

#links for each website
ocha_link = "https://data.humdata.org/dataset?q=haiti"
amerigeoos_link = "https://data.amerigeoss.org/gl/group/amerigeoss?q=haiti"





app = Flask(__name__)

@app.route('/datasets',  methods =["GET", "POST"])
def result():
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
    return render_template("news.html")

@app.route('/',  methods =["GET", "POST"])
def home():
    exchange_rate = Exchange_rate()
    front_news = HaitiLibre()
    
    return render_template("home.html",  rate = exchange_rate, articles = front_news.articles)

if __name__ == '__main__':
    app.run(debug = True)