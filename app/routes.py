from flask import Blueprint
import datetime

system_info = Blueprint('system_info', __name__)

@system_info.route('/v1')
def hello():
    return {
        "version": "v1",
        "timestamp": str(datetime.datetime.now()),
        "greeting": "Hello world!"
    }

