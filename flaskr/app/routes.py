from flask import render_template
from app import app #app is the member of app package
#which is defined in package imitial file



@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Hang'}
	return render_template('index.html', user = user)
