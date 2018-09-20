from flask import Flask

app = Flask(__name__)

#First Route
@app.route("/")
def hello():
    return "Hello World!"


#Second Route
@app.route("/2")
def how():
    return "This is new."

#Third Route
@app.route("/3")
def interesting():
    return "Very interesting."

if (__name__ == "__main__"):
    app.run(port = 5000)

    

#Run the python script using -

#python hello.py
