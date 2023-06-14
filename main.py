from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from mysqlclient import MySQLdb

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:@localhost/html?charset=utf8mb4
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(255), nullable=False)

@app.route("/")
def home():
    title = "Welcome to Html Tuts"
    return render_template("index.html", document=title)

@app.route("/course")
def course():
    return render_template("html-course.html")

@app.route("/html")
def html():
    return render_template("html.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        """Add Entry to the database"""
        name = request.form.get("name")
        email = request.form.get("email").strip()
        phone = request.form.get("phone")
        message = request.form.get("msg")
        entry = Contacts(name=name, phone_num=phone, email=email, msg=message)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
