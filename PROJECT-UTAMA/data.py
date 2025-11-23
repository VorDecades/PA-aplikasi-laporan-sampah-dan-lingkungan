from datetime import datetime

users = {
    "manager": {"password": "manager123", "role": "manager"},
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "ajis": {"password": "ajis123", "role": "woi"}
}

laporan = {}
log_activity = []
log_status = {}

def timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M")

def load_dummy():
    try:
        with open("load_dummy.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:  # skip header
                parts = line.strip().split(";")  # pakai ; sebagai delimiter
                if len(parts) < 7:
                    continue
                id, lokasi, jenis, deskripsi, status, user, tanggal = parts
                laporan[id] = {
                    "lokasi": lokasi,
                    "jenis": jenis,
                    "deskripsi": deskripsi,
                    "status": status,
                    "User": user
                }
                log_status[id] = tanggal
    except FileNotFoundError:
        print("File load_dummy.csv tidak ditemukan.")

