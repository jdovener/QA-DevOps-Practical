from application import app 
from flask import render_template
import requests

@app.route('/')
def index():
    chars = requests.get('http://service2:5000/get_text').text
    num = requests.get('http://service3:5000/get_nums').text
    prize = requests.post('http://service4:5000/prize', json=dict(chars=chars, num=num))
    return render_template('home.html', prize = prize.text)