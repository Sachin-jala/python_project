from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        category = request.form["category"]
        amount = float(request.form["amount"])
        db.session.add(Expense(title=title, category=category, amount=amount))
        db.session.commit()
        return redirect("/")
    rows = Expense.query.all()
    # Aggregate by category
    totals = {}
    for r in rows:
        totals[r.category] = totals.get(r.category, 0.0) + r.amount
    return render_template("index.html", rows=rows, totals=totals)

@app.route("/delete/<int:rid>", methods=["POST"])
def delete(rid):
    r = Expense.query.get_or_404(rid)
    db.session.delete(r)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)