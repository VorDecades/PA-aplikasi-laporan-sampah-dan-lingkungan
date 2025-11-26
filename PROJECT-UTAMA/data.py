from datetime import datetime

users = {
    "manager": {"password": "manager123", "role": "manager"},
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "ajis": {"password": "ajis123", "role": "woi"}
}

<<<<<<< HEAD
laporan = {} # menyimpan data laporan
log_activity = [] # menyimpan log aktivitas login
report_activity = [] # menyimpan log aktivitas laporan
log_status = {} # menyimpan log status laporan
=======
laporan = {} #menyimpan data laporan
log_activity = [] #log login
report_activity = [] #log laporan
log_status = {} #log status laporan
>>>>>>> e1e9491e12c4c9dfbf10d35423f1983b14f347a3

def timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M") # format tanggal dan waktu

def add_report_activity(id, before, after, actor):
    report_activity.append({
        "id": id,
        "before": before,
        "after": after,
        "actor": actor,
        "time": timestamp()
    })

def load_dummy():
    try:
<<<<<<< HEAD
        # mencari file dan memastikan file ada
        with open("load_dummy.csv", "r", encoding="utf-8") as f: 
=======
        with open("load_dummy.csv", "r", encoding="utf-8") as f:
>>>>>>> e1e9491e12c4c9dfbf10d35423f1983b14f347a3
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(";")
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