from flask import Flask, render_template
# use templates folder to host html
# use static folder to host css, img, video
# To make a web page editable
#   inspect -> console -> document.body.contentEditable = true

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)