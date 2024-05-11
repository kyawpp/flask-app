from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SystemInfo(db.Model):
    __tablename__ = 'system_info'

    id = db.Column(db.Integer, primary_key=True)
    os_info = db.Column(db.String)
    cpu_utilization = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    ip = db.Column(db.String)

    def __init__(self, os_info, cpu_utilization, ip):
        self.os_info = os_info
        self.cpu_utilization = cpu_utilization
        self.ip = ip
