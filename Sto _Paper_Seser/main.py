from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Serve the frontend
@app.route("/")
def home():
    return render_template("frontend.html")

# API endpoint for playing the game
@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    you = data.get("choice")

    youDict = {'s': 1, 'p': -1, 'k': 0}  # s = stone, p = paper, k = seser
    reversDict = {1: 'stone', -1: 'paper', 0: 'seser'}

    computer = random.choice([1, -1, 0])
    you = youDict[you]

    if computer == you:
        result = "draw"
        msg = "It's a tie!"
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        result = "win"
        msg = "You win!"
    else:
        result = "lose"
        msg = "You lose!"

    return jsonify({
        "player": reversDict[you],
        "computer": reversDict[computer],
        "result": result,
        "message": msg
    })

if __name__ == "__main__":
    app.run(debug=True)
