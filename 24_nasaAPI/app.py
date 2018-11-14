import urllib.request
from flask import Flask, render_template, request

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def reroute():
        u = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=31YHWQTWUpAhvwiZvXegOzVSmQ6u084ploE74SxV')
        html = u.read()
        return render_template("index.html", img="")

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
