from flask import Flask, render_template, session, redirect, request, url_for

app = Flask(__name__)
app.secret_key = "dev-secret-key"

PRODUCTS = [
    {"id": 1, "name": "T-Shirt", "price": 499},
    {"id": 2, "name": "Headphones", "price": 1999},
    {"id": 3, "name": "Backpack", "price": 1299},
]

def get_cart():
    return session.setdefault("cart", {})

@app.route("/")
def index():
    cart = get_cart()
    total = sum(next(p['price'] for p in PRODUCTS if p['id']==int(pid)) * qty for pid, qty in cart.items())
    return render_template("index.html", products=PRODUCTS, cart=cart, total=total)

@app.route("/add/<int:pid>", methods=["POST"])
def add(pid):
    cart = get_cart()
    cart[str(pid)] = cart.get(str(pid), 0) + 1
    session["cart"] = cart
    return redirect(url_for("index"))

@app.route("/remove/<int:pid>", methods=["POST"])
def remove(pid):
    cart = get_cart()
    if str(pid) in cart:
        cart[str(pid)] -= 1
        if cart[str(pid)] <= 0:
            del cart[str(pid)]
        session["cart"] = cart
    return redirect(url_for("index"))

@app.route("/checkout", methods=["POST"])
def checkout():
    session["cart"] = {}
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)