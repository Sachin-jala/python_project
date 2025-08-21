from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Game state
number = random.randint(1, 100)
guesses = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess_number():
    global number, guesses
    data = request.json
    user_guess = int(data["guess"])
    guesses += 1

    if user_guess > number:
        return jsonify({"message": "⬇️ Lower number please", "success": False, "guesses": guesses})
    elif user_guess < number:
        return jsonify({"message": "⬆️ Higher number please", "success": False, "guesses": guesses})
    else:
        return jsonify({
            "message": f"🎉 You guessed it! The number was {number}. Attempts: {guesses}",
            "success": True,
            "guesses": guesses
        })

@app.route("/reset", methods=["POST"])
def reset_game():
    global number, guesses
    number = random.randint(1, 100)
    guesses = 0
    return jsonify({"message": "🔄 New game started! Guess a number between 1 and 100."})

if __name__ == "__main__":
    app.run(debug=True)
