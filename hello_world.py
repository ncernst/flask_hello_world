from flask import Flask
from os import environ

app = Flask(__name__)


@app.route("/hello/<name>")
def hi_person(name):
    html = """
    <h1>
        Hello {}!
    </h1>
    <p>
        Here's a picture of a kitten.
    </p>
    <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/jedi/<first>/<last>")    
def hello_jedi(first, last):
    jediName = "{0}{1}".format(last[0:3], first[0:2])
    
    html = """
    <p>Your Jedi name is:</p>
    <h1>{}!</h1>
    """
    return html.format(jediName.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))
