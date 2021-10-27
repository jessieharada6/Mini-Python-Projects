from flask import Flask, render_template
import requests
from post import Post

all_books = requests.get("https://api.npoint.io/669c6079d0f5906d577f").json()
book_list = []
for book in all_books:
    a_book = Post(book["id"], book["title"], book["authors"], book["body"])
    book_list.append(a_book)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", books = book_list)

@app.route('/blog/<int:id>')
def blog(id):
    which_book = None
    for book in book_list:
        if int(book.id) == id:
            which_book = book
    return render_template("post.html", book = which_book)

if __name__ == "__main__":
    app.run(debug=True)
