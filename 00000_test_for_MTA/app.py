import urllib.request, json
from flask import Flask, render_template
from util import parse_API

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def reroute():
        #https://www.googleapis.com/books/v1/users/<your-user-id>/bookshelves/<as-coll-id>?key=<api-key>
        #key=AIzaSyBw_R-7c6M1aK6BlLozMRxgoNDdOu0TCWY
        url='http://datamine.mta.info/mta_esi.php?key=968a25660a23f3e376618527d7844440'
        with urllib.request.urlopen(url) as testfile, open('dataset.json', 'w') as f:
            f.write(testfile.read().decode())
        #img=parse_API.image()
        return "nani"
if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
