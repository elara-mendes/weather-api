from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>/")
def request(station, date):
    temperature = 34
    data = {
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return data

if __name__ == "__main__":
    app.run(debug=True)