from flask import Flask, render_template, request, jsonify
import datetime as dt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/ask")
def ask():
    q = (request.json or {}).get("q","").lower()
    if "time" in q:
        a = f"The time is {dt.datetime.now().strftime('%H:%M')}"
    elif "date" in q:
        a = f"Today's date is {dt.date.today().isoformat()}"
    elif "your name" in q:
        a = "I'm your web voice assistant."
    else:
        a = f"You said: {q}"
    return jsonify({"answer": a})

if __name__ == "__main__":
    app.run(debug=True)