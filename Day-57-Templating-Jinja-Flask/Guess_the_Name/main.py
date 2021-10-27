import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome"

@app.route("/guess/<name>")
def home(name):
    param = {"name": name}
    response_age = requests.get("https://api.agify.io", params=param)
    response_age_in_json = response_age.json()
    age = response_age_in_json["age"]
    response_gender = requests.get("https://api.genderize.io", params=param)
    response_gender_in_json = response_gender.json()
    gender = response_gender_in_json["gender"]
    return render_template("index.html", age = age, gender = gender, name = name)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog = requests.get("https://api.npoint.io/669c6079d0f5906d577f")
    all_posts = blog.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug = True)


