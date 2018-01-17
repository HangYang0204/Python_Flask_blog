from app import app #app is the member of app package
#which is defined in package imitial file



@app.route('/')
@app.route('/index')
def index():
	return "Hello Hang!"