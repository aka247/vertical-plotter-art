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

my_email = os.environ.get('MY_EMAIL')
my_email_pwd = os.environ.get('MY_EMAIL_PWD')

# APP ######################################
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET')
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
    art_path = os.path.join(app.static_folder, "assets", "img", "art")
    projects = []

    for folder in sorted(os.listdir(art_path)):
        folder_path = os.path.join(art_path, folder)
        print(f"Checking folder: {folder_path}")
        if os.path.isdir(folder_path):
            files = sorted(os.listdir(folder_path))
            # print(f"Processing folder: {folder}")
            files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp','.mp4', '.mov', '.webm'))]
            
            if files:
                preview = f'assets/img/art/{folder}/{files[0]}'  # first image as preview
                # print(f"Preview files: {preview}")
            else:
                continue

            projects.append({
                "name": folder,
                "preview": preview, # first image or video as preview
                "files": files,
            })
            # print (f"project.name: {folder}, project.preview: {preview}, project.files: {files}")

    return render_template("index.html", projects=projects)


if __name__ == "__main__":
    app.run( debug=True, port=5017)
