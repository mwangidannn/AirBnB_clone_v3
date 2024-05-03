#!/usr/bin/python3
...
Create Flask app;app_views
...
from flask import jsonify
from api3.v1.sviews import app_views

@app_views.route('/status',)
def api_status():
    """

    """
    response = {'status': "OK"}
    return jsonify(responses)
