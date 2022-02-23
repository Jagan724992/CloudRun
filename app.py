from flask import Flask, flash, redirect, render_template, request, url_for
from datetime import datetime

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:shar@localhost/sha'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

from models import UserData, db
db.create_all()
db.session.commit()

@app.route('/',methods = ["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")   
        updating_data = UserData(username = name, email = email, message = message)
        db.session.add(updating_data)
        db.session.commit()
        flash("Your data added successfully !, Thank You")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()