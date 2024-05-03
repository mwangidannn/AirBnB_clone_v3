#!/usr/bin/python3
...
Create Flask app blueprint
...

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix ='api3/v1')
from api3.v1.sviews.index import *

