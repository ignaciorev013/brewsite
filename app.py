from flask import Flask, render_template

app = Flask(__name__)

# Mock brewery data for Jinja templating
breweries_data = [
    {
        "name": "High Desert Brewing Co.",
        "city": "Las Cruces",
        "state": "NM",
        "type": "Microbrewery",
        "website": "https://highdesertbrewingco.com"
    },
    {
        "name": "Bosque Brewing Co.",
        "city": "Las Cruces",
        "state": "NM",
        "type": "Regional Brewery",
        "website": "https://www.bosquebrewing.com"
    },
    {
        "name": "Spotted Dog Brewery",
        "city": "Mesilla",
        "state": "NM",
        "type": "Brewpub",
        "website": "https://spotteddogbrewery.com"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/brewery")
@app.route("/breweries")
def brewery():
    return render_template("brewery.html", breweries=breweries_data)

if __name__ == "__main__":
    app.run(debug=True)