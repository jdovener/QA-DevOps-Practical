from application import app
from flask import Response
import random

@app.route('/get_activity', methods=['GET'])
def activity():
    activity = random.choice(["Mini-Golf", "Axe-Throwing", "Escape-Room", "Rock-Climbing", "Ice-Skating"])
    return Response(activity, mimetype='text/plain')

