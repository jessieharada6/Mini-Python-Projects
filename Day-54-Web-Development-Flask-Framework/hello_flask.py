# importantly, don't create a file name that is the same as the library

# to run flask
#export FLASK_APP={file-name}.py
#flask run

from flask import Flask
from markupsafe import escape
app = Flask(__name__)
#module name, if it shows "__main__", means it's running the current file
print(__name__)
#import random
#print(random.__name__)

# flask determines which routes to call
#/ is home address
# only trigger this function if the url is home address
#@ is python decorator, lives in the app project, declared in line 8 app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Goodbye"

# <variable_name?
@app.route("/username/<name>")
def greet(name):
    return f"hello {name}"

@app.route("/<name>")
def greet_name(name):
    return f"hi there {name}"

@app.route("/username/<name>/1")
def greet_name_1(name):
    return f"hi again {name}"

# <converter:variable_name>.
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return 'Post %d' %post_id

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'
# top level code => __main__ (name of scope)

@app.route("/username/<name>/<int:age>")
def show_info(name, age):
    return f"you are {name}, and you are {age} years old"

if __name__ == "__main__":
    # activate debugger
    # 1. any changes made can be updated without restart -- auto reload
    # 2. show the error on the web page
    app.run(debug=True)
