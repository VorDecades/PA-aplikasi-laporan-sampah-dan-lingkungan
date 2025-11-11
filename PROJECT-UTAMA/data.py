from datetime import datetime

users = {
    "manager": {"password": "manager123", "role": "manager"},
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "ajis": {"password": "ajis123", "role": "woi"}
}

laporan = {}
log_status = {}

def timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M")
