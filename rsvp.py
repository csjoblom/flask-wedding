import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response
from dbhandling import db_session
from models import Guest

app = Flask(__name__)
app.config.from_object('default_settings')

@app.before_request
def before_request():
	db_session()

@app.teardown_request
def teardown_request(exception=None):
	db_session.remove()

@app.route('/ceremony')
def ceremony():
	return render_template('ceremony.html')

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/firstdate')
def firstdate():
	return render_template('firstdate.html')

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

@app.route('/weddingparty')
def weddingparty():
	return render_template('weddingparty.html')

@app.route('/info')
def info():
	return render_template('info.html')

@app.route('/registry')
def registry():
	return render_template('registry.html')

@app.route('/rsvplist')
def show_entries():
	guests = Guest.query.all()
	return render_template('rsvplist.html', guests=guests) 

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
	error = None
	formfilled = request.cookies.get('rsvpstat')
	if formfilled == '1':
		return redirect(url_for('thankyou'))
	if request.method == 'POST':
			if 'inputName' in request.form:
				if request.form['inputName'] == '':
					error = "Name field cannot be blank."
					return render_template('rsvp.html', error=error)
				else:
					inputName = request.form['inputName']
			if 'inputGuest' in request.form:
				inputGuest = request.form['inputGuest']
			if 'inputEmail' in request.form:
				inputEmail = request.form['inputEmail']
			if 'decision' in request.form:
				if request.form['decision'] == 'attending':
					inputDecision = "Yes" 
				else:
					inputDecision = "No"
			if 'inputComment' in request.form:
				inputComment = request.form['inputComment']
			guest = Guest(name=inputName, email=inputEmail, invitename=inputGuest, comments=inputComment, decision=inputDecision)
			db_session.add(guest)
			db_session.commit()
			#flash(message)
			resp = make_response(redirect(url_for('thankyou')))
			resp.set_cookie('rsvpstat', '1')
			return resp
	return render_template('rsvp.html', error=error)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
