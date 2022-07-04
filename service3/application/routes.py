from application import app
from flask import Response
import random

@app.route('/get_location', methods=['GET'])
def location():
    location = random.choice(["Manchester", "Leeds", "Scotland", "London"])
    return Response(location, mimetype='text/plain')