"""
Personal Blog
Author: Andrea Klostermann
Date : 27.12.2024
"""

import random
import datetime
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request, make_response
from flask_bootstrap import Bootstrap # Bootstrap5
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib
import os
import io
#from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm, StocksForm, InteractiveMap

my_email = "a_k@gmx.at" # os.environ.get('MY_EMAIL')
my_email_pwd = "32434432" # os.environ.get('MY_EMAIL_PWD')

# APP ######################################
app = Flask(__name__)
app.config['SECRET_KEY'] = "jskfdljdsflkjdslf" #= os.environ.get('APP_SECRET')
Bootstrap(app)
#Bootstrap5(app)


############################################
# Show Contact Site
# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         send_email(data)

#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)


# mail senden
def send_email(data):
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]

    email_content = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        # tls to secure connection
        connection.starttls()
        connection.login(user=my_email, password=my_email_pwd)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=email_content.encode('utf-8'))


# Shows About Site #######################################
@app.route("/about")
def about():
    return render_template("about.html")

# Home #######################################
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run( debug=True, port=5017)
