# importantly, don't create a file name that is the same as the library

# to run flask
#export FLASK_APP={file-name}.py
#flask run

from flask import Flask
app = Flask(__name__)
#module name, if it shows "__main__", means it's running the current file
print(__name__)
#import random
#print(random.__name__)

# flask determines which routes to call
#/ is home address
# only trigger this function if the url is home address
#@ is python decorator
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Goodbye"

# top level code => __main__ (name of scope)
if __name__ == "__main__":
    app.run()
