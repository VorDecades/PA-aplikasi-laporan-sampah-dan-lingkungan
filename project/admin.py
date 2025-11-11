import os
from InquirerPy import inquirer
from prettytable import PrettyTable
from data import laporan, log_status, timestamp

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_laporan():
    clear()
    try:
        print("=== DAFTAR LAPORAN ===")
        if not laporan:
            print("Belum ada laporan.")
            input("\nTekan Enter")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Lokasi", "Jenis", "Status", "Deskripsi", "Tanggal"]
        for id, data in laporan.items():
            table.add_row([
                id, data["lokasi"], data["jenis"], data["status"],
                data["deskripsi"], log_status.get(id, "Belum ada")
            ])
        print(table)
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def buat_laporan(username):
    clear()
    try:
        print("=== CREATE LAPORAN ===")
        lokasi = input("Lokasi kejadian: ").strip()
        if not lokasi:
            raise ValueError("Lokasi tidak boleh kosong.")

        jenis = inquirer.select(
            message="Pilih jenis masalah:",
            choices=["sampah", "pencemaran", "perusakan"],
            pointer="👉"
        ).execute()

        deskripsi = input("Deskripsi singkat: ").strip()
        if not deskripsi:
            raise ValueError("Deskripsi tidak boleh kosong.")

        id = str(len(laporan) + 1)
        laporan[id] = {
            "lokasi": lokasi,
            "jenis": jenis,
            "deskripsi": deskripsi,
            "status": "belum ditindak",
            "dibuat_oleh": username
        }
        log_status[id] = timestamp()
        print("Laporan berhasil dibuat.")
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def update_laporan():
    clear()
    try:
        print("=== UPDATE STATUS LAPORAN ===")
        id = input("Masukkan ID laporan: ").strip()
        if id not in laporan:
            raise ValueError("ID tidak ditemukan.")

        status_baru = inquirer.select(
            message="Pilih status baru:",
            choices=["belum ditindak", "di proses", "sudah ditindak"],
            pointer="👉"
        ).execute()

        laporan[id]["status"] = status_baru
        log_status[id] = timestamp()
        print("Status berhasil diperbarui.")
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def hapus_laporan():
    clear()
    try:
        print("=== HAPUS LAPORAN ===")
        id = input("Masukkan ID laporan: ").strip()
        if id not in laporan:
            raise ValueError("ID tidak ditemukan.")

        konfirmasi = inquirer.confirm("Yakin ingin menghapus laporan ini?", default=False).execute()
        if konfirmasi:
            del laporan[id]
            log_status.pop(id, None)
            print("Laporan dihapus.")
        else:
            print("Dibatalkan.")
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
