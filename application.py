from flask import Flask, redirect, render_template
from flask import send_file

app=Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

# @app.route("/profie_img")
# def profie_img():
# 	return render_template(".\\assets\\profile.jpg")


if __name__=="__main__":
	app.run(debug=True)


