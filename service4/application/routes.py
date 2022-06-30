from application import app
from flask import request
from random import choice

@app.route('/prize', methods=['POST'])
def prize():
    data_sent = request.get_json()
    if data_sent['chars'][0] == 'a':
        prizes = ([50] * 3) + [100]
        prize = '£' + str(choice(prizes))
        return prize
    elif int(data_sent['num']) % 2 == 0:
        return "£20"
    else:
        return "No Prize"