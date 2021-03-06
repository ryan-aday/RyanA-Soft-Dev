# Tina Wong, Ryan Aday
# Team TL;DR
# SoftDev1 pd7
# K15 -- Do I Know You?
# 2018-10-02

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask(__name__) #create instance of class Flask
app.secret_key = os.urandom(32)  #creates random key of 32 bytes

users = {'test' : '123'}  #key and dict

# home page that links to the form
@app.route("/") #assign fxn to route
def home():
    # print("testing")
    if 'test' not in session:
        return render_template("login.html")
    else:
        user = 'test'
        return render_template("welcome.html",user=user)

# a route that receives the form and returns a template with user's information
@app.route("/auth", methods=["POST"]) #assign fxn to route
def authenticate():
    if request.form['username'] not in users.keys():
        flash("Error with username")
        return render_template("login.html")
        #Returns login with Username error
    
    elif users[request.form['username']] != request.form['password']:
        flash("Error with password")
        return render_template("login.html")
        #Returns login with Password error

    else:
        session['test'] = '123'
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('test')  #Ends session
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
