# ULUNG
import os
from termcolor import colored
from InquirerPy import inquirer
from tabulate import tabulate
from data import laporan, log_status, timestamp, add_report_activity

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

def MENU_ADMIN(username):
    clear()
    while True:
        try:
            width = 45  
            print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
            print(colored("[ MENU ADMIN ]".center(width), "yellow"))
            print(colored(f"[ SELAMAT DATANG {username} ]".center(width), "yellow"))
            print(colored("=" * width + "\033[0m", "yellow"))
            menu = inquirer.select(
                message=("Pilih Menu yang Ingin Diakses: "),
                choices=["Tampilkan Semua Laporan", "Tampilkan Laporan Filter", "Buat Laporan", "Update Status", "Hapus Laporan", "Logout"],
                pointer="👉"
            ).execute()

            if menu == "Tampilkan Semua Laporan":
                READ()
            elif menu == "Tampilkan Laporan Filter":
                FILTER_READ()
            elif menu == "Buat Laporan":
                CREATE(username)
            elif menu == "Update Status":
                UPDATE()
            elif menu == "Hapus Laporan":
                DELETE()
            elif menu == "Logout":
                break
        except Exception as e:
            print(colored(f"\nError: {e}", "red"))
            pause()

def READ():
    clear()
    try:
        width = 110
        print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
        print(colored("[ DAFTAR SEMUA LAPORAN ]".center(width), "yellow"))
        print(colored("=" * width + "\033[0m", "yellow"))
    
        if not laporan:
            print(colored("Belum Ada Laporan.", "red"))
            pause()
            clear()
            return

        headers = ["ID", "Lokasi", "Jenis", "Status", "Deskripsi", "Tanggal", "User"]
        rows = [
            [id, data["lokasi"], data["jenis"], data["status"],
            data["deskripsi"][:20] + "...", log_status.get(id, "Belum ada"), data["User"]]
            for id, data in laporan.items()
        ]
        print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
        pause()
        clear()
    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()


def FILTER_READ():
    clear()
    try:
        width = 112  
        print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
        print(colored("[ FILTER LAPORAN BERDASARKAN STATUS ]".center(width), "yellow"))
        print(colored("=" * width + "\033[0m", "yellow"))
        status_filter = inquirer.select(
            message="Pilih Status Laporan yang Ingin Ditampilkan:",
            choices=["belum ditindak", "di proses", "sudah ditindak"],
            pointer="👉"
        ).execute()

        filtered = {
            id: data for id, data in laporan.items()
            if data["status"] == status_filter.lower()
        }

        if not filtered:
            print(colored(f"Tidak Ada Laporan Dengan Status '{status_filter}'.", "red"))
        else:
            headers = ["ID", "Lokasi", "Jenis", "Status", "Deskripsi", "Tanggal", "User"]
            rows = [
                [id, data["lokasi"], data["jenis"], data["status"],
                data["deskripsi"], log_status.get(id, "Belum ada"), data["User"]]
                for id, data in filtered.items()
            ]
            print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

        pause()
        clear()

    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()
        clear()

def CREATE(username):
    clear()
    try:
        width = 45  
        print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
        print(colored("[ BUAT LAPORAN ]".center(width), "yellow"))
        print(colored("=" * width + "\033[0m", "yellow"))
        lokasi = input("Lokasi kejadian: ").strip()
        if not lokasi:
            raise ValueError(colored("Lokasi Tidak Boleh Kosong.", "red"))

        jenis = inquirer.select(
            message="Pilih Jenis Masalah:",
            choices=["sampah", "pencemaran", "perusakan"],
            pointer="👉"
        ).execute()

        deskripsi = input("Deskripsi Singkat: ").strip()
        if not deskripsi:
            raise ValueError("Deskripsi Tidak Boleh Kosong.")

        id = str(len(laporan) + 1)
        laporan[id] = {
            "lokasi": lokasi,
            "jenis": jenis,
            "deskripsi": deskripsi,
            "status": "belum ditindak",
            "User": username
        }
        log_status[id] = timestamp()
        add_report_activity(id, None, "belum ditindak", username)

        print(colored("Laporan Telah Berhasil Dibuat.", "green"))
        pause()
        clear()

    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()
        clear()

#IHSAN
def UPDATE():
    clear()
    try:
        width = 45  
        print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
        print(colored("[ UPDATE STATUS LAPORAN ]".center(width), "yellow"))
        print(colored("=" * width + "\033[0m", "yellow"))
        lokasi = input("Lokasi kejadian: ").strip()
        id = input("Masukkan ID Laporan: ").strip()
        if id not in laporan:
            raise ValueError(colored("ID Tidak Ditemukan.", "red"))

        status_baru = inquirer.select(
            message="Pilih Status Baru:",
            choices=["belum ditindak", "di proses", "sudah ditindak"],
            pointer="👉"
        ).execute()

        before = laporan[id]["status"]
        laporan[id]["status"] = status_baru
        log_status[id] = timestamp()
        add_report_activity(id, before, status_baru, "admin")

        print(colored("Status Berhasil Diperbarui.", "green"))
        pause()
        clear()

    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()
        clear()

def DELETE():
    clear()
    try:
        width = 45  
        print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
        print(colored("[ HAPUS LAPORAN ]".center(width), "yellow"))
        print(colored("=" * width + "\033[0m", "yellow"))
        lokasi = input("Lokasi kejadian: ").strip()
        id = input("Masukkan ID Laporan: ").strip()
        if id not in laporan:
            raise ValueError("ID Tidak Ditemukan.")

        konfirmasi = inquirer.confirm("Apakah Anda Yakin Ingin Menghapus Laporan Ini?", default=False).execute()
        if konfirmasi:
            before = laporan[id]["status"]
            del laporan[id]
            log_status.pop(id, None)
            add_report_activity(id, before, None, "admin")
            print(colored("Laporan Dihapus.", "red"))
        else:
            print(colored("Dibatalkan.", "yellow"))
        pause()
        clear()

    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()
        clear()
