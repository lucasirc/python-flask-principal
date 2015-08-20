from flask import Flask, render_template
from flask.ext.login import LoginManager, login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "123123123"

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/admin')
@login_required
def admin():
	return render_template('admin.html')

if __name__ == '__main__':
	print "INIT FLASK"

	use_debugger = True
	app.run(use_debugger=use_debugger, debug=use_debugger)