
#* IMPORTING FLASK

########################################
from flask import Flask, Blueprint, render_template, url_for, redirect
########################################

#* DEFINING FLASK 

########################################

app = Flask(__name__)

########################################

#* FLASK APPS 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/trending")
def trending_page():
    return render_template("trending.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/contact")
def contactus_page():
    return render_template("contact.html")


@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))



########################################

#* Error handling

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500

########################################

#* ADDING DEBUGGING

########################################

if __name__ == "__main__":
    app.run(debug=True, port=8000)