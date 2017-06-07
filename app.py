from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
import config
import os
import datetime

app = Flask(__name__)
client = MongoClient('mongodb://test:test@ds115352.mlab.com:15352/flask-register')
db = client['flask-register']
app.debug = True

class User():
	def __init__(self, username, email, password):
		self.username= username
		self.email = email
		self.password = password
		self.approved = False
		self.authenticated= False
		self.admin_status = False

	def resp(self):
		return {"username": self.username, "email": self.email, "password": self.password, \
				"approved": self.approved, "authenticated" : self.authenticated, \
				"admin_status": self.admin_status, "date": datetime.datetime.utcnow() }


@app.route("/")
def index():
	return render_template('base.html')
	
@app.route("/login",methods = ['POST', 'GET'] )
def login():
	if request.method == 'POST':
		emailid = request.form['inputEmail']
		
	return render_template('login.html')

@app.route("/signup",methods = ['POST', 'GET'] )
def signup():
	if request.method == 'POST':
		emailid = request.form['inputEmail']
		password = request.form['inputPassword']
		username = request.form['username']
		new_user = User(username, emailid, password)
		user = db.user
		user.insert(new_user.resp())
		return redirect(url_for('login'))
	return render_template('signup.html')
	
if __name__ == "__main__":
    app.run()
