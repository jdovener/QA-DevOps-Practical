from application import app
from flask import request, Response
import random

@app.route('/cost', methods=['POST'])
def cost():
    activity_data = request.get_json()
    activity = activity_data["activity"]
    location = activity_data["location"]
    activities = {"Mini-Golf": 15, "Axe-Throwing": 20, "Escape-Room": 35, "Rock-Climbing": 30, "Ice-Skating": 20}
    locations = {"Manchester": 0, "Leeds": 20, "Scotland": 35, "London": 45}
    cost = f"{activity} in {location}! Which will cost: £{activities[activity] + locations[location]}"
    return Response(cost, mimetype='text/plain')