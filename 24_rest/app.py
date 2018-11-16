#Ryan Aday
#K26 - APIs
#Period 7
#2018-11-14

import urllib.request
import json
from flask import Flask, render_template
from util import parse_API

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def reroute():
        url='https://api.nasa.gov/planetary/apod?api_key=31YHWQTWUpAhvwiZvXegOzVSmQ6u084ploE74SxV'
        with urllib.request.urlopen(url) as testfile, open('dataset.json', 'w') as f:
            f.write(testfile.read().decode())
        title=parse_API.title()
        video=parse_API.video()
        explanation=parse_API.explanation()
        version=parse_API.version()
        media_type=parse_API.media_type()
        return render_template("index.html", video=video, title=title, explanation=explanation, version=version, media_type=media_type)

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
