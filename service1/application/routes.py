from application import app 
from flask import render_template
import requests

@app.route('/')
def index():
    activity = requests.get('http://service2:5000/get_activity').text
    location = requests.get('http://service3:5000/get_location').text
    cost = requests.post('http://service4:5000/cost', json=dict(activity=activity, location=location))
    return render_template('home.html', cost = cost.text)