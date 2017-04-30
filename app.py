from flask import Flask, render_template, url_for, request
import config
import os

app = Flask(__name__)
app.debug = False

@app.route("/")
def index():
	return render_template('base.html')
	
@app.route("/signin",methods = ['POST', 'GET'] )
def signin():
	if request.method == 'POST':
		emailid = request.form['inputEmail']
		print(emailid)
	return render_template('signin.html')

@app.route("/signup",methods = ['POST', 'GET'] )
def signup():
	if request.method == 'POST':
		emailid = request.form['inputEmail']
		name = request.form['inputName']
		collegeid = request.form['inputId']
	return render_template('signup.html')
	
if __name__ == "__main__":
    app.run()
