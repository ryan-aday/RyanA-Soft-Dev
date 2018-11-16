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

        weather='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22nome%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
        with urllib.request.urlopen(weather) as testfile, open('data_weather.json', 'w') as f:
            f.write(testfile.read().decode())
        imageWeather=parse_API.imageWeather()

        #img_dog=parse_API.imageDog()

        return render_template("index.html", comic_image=img_XKCD, dog_image=img_dog, weather=imageWeather)
if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
