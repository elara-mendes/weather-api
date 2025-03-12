from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>/")
def request(station, date):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    stations_df = pd.read_csv("data-small/stations.txt", skiprows=17)
    # print(df)
    name = stations_df.loc[stations_df["STAID"] == int(station)]["STANAME                                 "].values[0]
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    data = {
        "name": name,
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return data


if __name__ == "__main__":
    app.run(debug=True)
