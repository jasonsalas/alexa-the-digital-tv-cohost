import logging
import os

from flask import Flask, render_template
from flask_ask import Ask, session, statement, question

__author__ = 'jason@kuam.com :: @jasonsalas :: jasonsalas671'

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
	return question(render_template('greeting'))

@ask.intent('RundownIntent')
def rundown():
	return statement(render_template('rundown'))

@ask.intent('FindMoreIntent')
def find_more():
	return statement(render_template('find_more'))

@ask.intent('StarWarsIntent')
def starwars():
	return statement(render_template('star_wars'))

@ask.intent('RideOrDieIntent')
def ride_or_die():
	return statement(render_template('ride_or_die'))

@ask.intent('BestieIntent')
def besties():
	return statement(render_template('besties'))

@ask.intent('ByeByeIntent')
def byebye():
	return statement(render_template('byebye'))

@ask.intent('KUAMTVScheduleIntent', default={'show':'the good life'})
def get_show_schedule(show):
	listings = { 'the malfunction show':'Sundays on t-v-8', 'the culture club':'Wednesdays at 6:30pm on k-u-a-m news extra', 'the good life':'New episode the first Sunday of each month on t-v-8 and t-v-11' }
	my_show = render_template('schedule', show_name=show, show_time=listings[show])
	return statement(my_show)

@ask.intent('AMAZON.StartOverIntent')
def startover():
	return launch()

'''
@ask.intent('AMAZON.CancelIntent')
def cancel():
	return statement(render_template('cancel_stop'))

@ask.intent('AMAZON.StopIntent')
def stop():
	return statement(render_template('cancel_stop'))

@ask.intent('AMAZON.HelpIntent')
def help():
	return question(render_template('be_a_guest'))
'''

@ask.session_ended
def session_ended():
	return '{}', 200

if __name__ == '__main__':
	if 'ASK_VERIFY_REQUESTS' in os.environ:
		verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
		if verify == 'false':
			app.config['ASK_VERIFY_REQUESTS'] = False
	app.run(debug=True)