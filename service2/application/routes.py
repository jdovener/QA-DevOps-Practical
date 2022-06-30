from application import app
from random import choice

@app.route('/get_text', methods=['GET'])
def get_text():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = ''.join(choice(alphabet) for _ in range(3))
    return text

