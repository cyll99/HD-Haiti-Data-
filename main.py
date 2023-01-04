from flask import Flask, render_template, request
from amerigeoos import Amerigeoos
from ocha import Ocha


ocha_link = "https://data.humdata.org/dataset?q=haiti"
amerigeoos_link = "https://data.amerigeoss.org/gl/group/amerigeoss?q=haiti"





app = Flask(__name__)

@app.route('/',  methods =["GET", "POST"])
def result():
    ocha = Ocha(ocha_link)
    amerigeoos = Amerigeoos(amerigeoos_link)

    ocha_data = zip(ocha.titles, ocha.descriptions, ocha.details)
    amerigeoos_data = zip(amerigeoos.titles, amerigeoos.descriptions, amerigeoos.details)
    # if request.method == "POST":
    #     # getting input_key in HTML form
    #     input_key = request.form.get("search")
    #     file_name = f"{path}/{input_key}.csv"
    #     notice = f'You will also find the result in {path}'
    #     download_data(input_key, file_name)
    #     with open(f"{path}/{input_key}_by_prices.csv", encoding="UTF-8") as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         return render_template('index.html', result = reader, notice=notice)
    return render_template("index.html", ocha = ocha_data, amerigeoos = amerigeoos_data)

if __name__ == '__main__':
    app.run(debug = True)