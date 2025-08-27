import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY") or "YOUR_API_KEY_HERE"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    city = ""
    error = None
    if request.method == "POST":
        city = request.form.get("city","").strip()
        if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
            error = "Set OPENWEATHER_API_KEY environment variable or put it in app.py."
        elif city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                weather = r.json()
            else:
                error = f"API error: {r.status_code}"
    return render_template("index.html", weather=weather, city=city, error=error)

if __name__ == "__main__":
    app.run(debug=True)