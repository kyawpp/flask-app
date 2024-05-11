from flask import Blueprint
from .models import SystemInfo, db

import psutil
import datetime
import platform
import psutil


system_info = Blueprint('system_info', __name__)

@system_info.route('/')
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

@system_info.route('/v3')
def get_system_info():
    os_info = platform.platform()
    cpu_utilization = psutil.cpu_percent()
    ip = 'localhost'

    system_info_entry = SystemInfo(os_info=os_info, cpu_utilization=cpu_utilization, ip=ip)
    db.session.add(system_info_entry)
    db.session.commit()

    return {
        "version": "v3",
        "timestamp": str(datetime.datetime.now()),
        "os_info": f'OS Version: {os_info}',
        "cpu_usage": f'CPU Utilization: {cpu_utilization}%'
    }
