from flask import Flask, render_template, request, redirect, url_for
import pymongo
import uuid

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://mongo:27017")
db = client["mydb"]
fnf_coll = db["fnf"]


@app.route("/")
def home():
    return render_template('index.html', members=fnf_coll.find())


@app.route("/fnf/create")
def create():
    return render_template('create.html')


@app.route("/fnf/save", methods=['POST'])
def save():
    name = request.form['name']
    relation = request.form['relation']
    phone = request.form['phone']
    email = request.form['email']

    data = {"name": name, "relation": relation, "phone": phone, "email": email}

    fnf_coll.insert_one(data)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
