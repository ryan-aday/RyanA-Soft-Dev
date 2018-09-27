from flask import Flask, render_template, request
import cgi
app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def reroute():
        return render_template("template.html")

@app.route('/auth')
def auth():
        #print (app)
        #print (request)
        #print (request.headers)
        print (request.method)
        #print (request.args)
        #print (request.form)
        return "Whomst"
        
if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()
