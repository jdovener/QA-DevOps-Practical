from application import application
from random import randint

@app.route('/get_nums', methods=['GET'])
def get_nums():
    num = randint(100000, 999999)
    return str(num)