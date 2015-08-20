import flask
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.login import LoginManager, login_required, login_user, logout_user

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


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin':
        # Login and validate the user.
        user = load_user(username)
        print user
        print user.is_active
        if user.is_active():
        	print 'foi if'
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        #if not next_is_valid(next):
        #    return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@login_manager.user_loader
def load_user(userid):
    return User(userid)

@login_manager.unauthorized_handler
def unauthorized():
    return "UNAUTHORIZED"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

class User():
	def __init__(self, id):
		print "init user" + id
		self.id = id
		self.authenticated = True
		self.active = True
		self.anonymous = False

	def is_active(self):
		print 'metodo'
		return self.is_active

	def is_authenticated(self):
		return self.is_authenticated

	def is_anonymous(self):
		return self.is_anonymous


	def get_id(self):
		return self.id


if __name__ == '__main__':
	print "INIT FLASK"

	use_debugger = True
	app.run(use_debugger=use_debugger, debug=use_debugger)