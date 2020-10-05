#IMPORTED STUFF
from flask import Flask, render_template, redirect, url_for, request, make_response, session
import os
from flask_mail import Mail,Message
import json,requests

app=Flask(__name__)

#ERROR ROUTE
@app.errorhandler(404)
def handl(error1):
	print(error1)
	return render_template("errorpage.asp")

#HOMEPAGE ROUTE
@app.route('/')
def home():
    return render_template("homepge3.asp")
    #epic code 
    #forget the codes features 

#NEWS ROUTE
@app.route('/news')
def newsret():
    return render_template("newspage.asp")
    #very big code
    #small change 

#RUNNING OF THE WEBSITE
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
