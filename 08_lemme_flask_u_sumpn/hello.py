from flask import Flask

app = Flask(__name__)

#First Route
#Main page, default on what you see in link
@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
        <head>
            <title>Hello, Main Page!</title>
        </head>
        <body>
            <p> To access the other pages, type in /link or /cool to the link. </p>
            <img src="http://www.ox.ac.uk/sites/files/oxford/styles/ow_medium_feature/public/field/field_image_main/Aliens.jpg" alt="cool pic"/>
        </body>
    </html>
    """

#Second Route
#Type in /link at end of link to access
@app.route("/link")
def link():
    return """
    <!DOCTYPE html>
        <head>
            <title>Links</title>
        </head>
        <body>
            <p> To access the other pages, remove the /links or type in /cool to the link. </p>
            <p>
            <a href="http://www.google.com">
              Google
            </a>
            </p>
            <p>
            <a href="http://www.stuycs.org">
              StuyCS
            </a>
            </p>
        </body>
    </html>
    """

#Third Route
#Type in /cool at end of link to access
@app.route("/cool")
def interesting():
    return """
    <!DOCTYPE html>
        <head>
            <title>Cool</title>
        </head>
        <body>
            <h1>Cool beans</h1>
            <p> To access the other pages, type in /link or remove /cool to the link. </p>
            <img src="https://i.kym-cdn.com/entries/icons/original/000/026/782/picB92GVL.jpg" alt="beans"/>
        </body>
    </html>
    """

if (__name__ == "__main__"):
    app.run(port = 5000) 

#Run the python script using -
#python hello.py
