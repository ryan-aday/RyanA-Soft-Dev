#Ryan Aday
#K26 - APIs
#Period 7
#2018-11-16


import urllib.request, json
from flask import Flask, render_template
from util import parse_API

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def reroute():

        xkcd='http://xkcd.com/info.0.json'
        with urllib.request.urlopen(xkcd) as testfile, open('data_xkcd.json', 'w') as f:
            f.write(testfile.read().decode())
        img_XKCD=parse_API.image_XKCD()

        dog='https://dog.ceo/api/breeds/image/random'
        with urllib.request.urlopen(dog) as testfile, open('data_dog.json', 'w') as f:
            f.write(testfile.read().decode())
        img_dog=parse_API.imageDog()

        cat='https://catfact.ninja/fact'
        with urllib.request.urlopen(cat) as testfile, open('data_cat.json', 'w') as f:
            f.write(testfile.read().decode())
        cat_Fact=parse_API.cat_Fact()

        #img_dog=parse_API.imageDog()

        return render_template("index.html", comic_image=img_XKCD, dog_image=img_dog, cat_Fact=cat_Fact)
if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
