#Ryan A.
#K10: Jinja Tuning
#Period 7
#2018-09-24

from flask import Flask, render_template
#imports my function from another python file
from occupations import combine

app=Flask(__name__)

@app.route("/")
def home():
    #added for people to know how to get to proper page
    return"""
        <DOCtype html>
        <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <p>To access the occupations part, add /occupations to your link.</p>
        </body>
        </html>
        """

@app.route("/occupations")
def choose():
    return render_template('temp.html', job=combine())

if __name__ == "__main__":
    app.debug=True
    app.run()
