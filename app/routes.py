from flask import Blueprint
import psutil
import datetime


system_info = Blueprint('system_info', __name__)

@system_info.route('/v1')
def hello():
    return {
        "version": "v1",
        "timestamp": str(datetime.datetime.now()),
        "greeting": "Hello world!"
    }

@system_info.route('/v2')
def os_info():
    cpu_percent = psutil.cpu_percent()
    return {
        "version": "v2",
        "timestamp": str(datetime.datetime.now()),
        "cpu_usage": f'CPU Usage: {cpu_percent}%'
    }
