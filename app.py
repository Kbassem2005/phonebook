import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = sqlite3("sqlite:///phonebook.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/delete", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM contacts WHERE id = ?", id)
    return redirect("/contacts")

@app.route("/add", methods=["POST"])
def register():
    name = request.form.get("name")
    phonenumber = request.form.get("phonenumber")

    db.execute("INSERT INTO contacts (name, phonenumber) VALUES(?, ?)",name, phonenumber)

    return redirect("/contacts")

@app.route("/contacts")
def contacts():
    contacts = db.execute("SELECT * FROM contacts")
    return render_template("contacts.html", contacts=contacts)

@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        contacts = db.execute("SELECT * FROM contacts WHERE name LIKE ?", "%" + q + "%")
    else:
        contacts = []
    return render_template("search.html", contacts=contacts)

@app.route("/searcht")
def searcht():
    return render_template("search.html")