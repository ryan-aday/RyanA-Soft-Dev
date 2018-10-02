#Ryan Aday
#SoftDev1 pd7
#K13 -- Echo
#2018-09-28 

from flask import Flask, render_template, request, session, url_for, redirect 

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def home():
        return render_template("main.html")


@app.route('/auth', methods=["GET"])
def auth():
        print (request.args["username"])
        if (request.args["username"] != "test" or request.args["password"]!="1234"):
                if (request.args["username"]!="test"):
                        print ("Username invalid")
                else:
                        print ("Password invalid")
                        
                return redirect(url_for("home"))
                
        return render_template("succ.html", username=request.args["username"])
        #All data from the form is carried over via the request.args() method

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
