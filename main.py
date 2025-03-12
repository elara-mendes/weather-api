from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations_df = pd.read_csv("data-small/stations.txt", skiprows=17)
id_name = stations_df[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=id_name.to_html())


@app.route("/api/v1/<station>/<date>/")
def request(station, date):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    name = stations_df.loc[stations_df["STAID"] == int(station)]["STANAME                                 "].values[0]
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    data = {
        "name": name,
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return data


@app.route("/api/v1/<station>/")
def station(station):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<date>/")
def date(station, date):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(date))].to_dict(orient="records")
    print(result)
    return result


if __name__ == "__main__":
    app.run(debug=True)
