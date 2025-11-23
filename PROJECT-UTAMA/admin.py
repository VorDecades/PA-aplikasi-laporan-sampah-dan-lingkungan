import os
from termcolor import colored
from InquirerPy import inquirer
from tabulate import tabulate
from data import laporan, log_status, timestamp

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

def MENU_ADMIN(username):
    clear()
    while True:
        try:
            menu = inquirer.select(
                message=("\n============================\n=== >>> [Menu Admin] <<< ===\n============================"),
                choices=["Tampilkan Semua Laporan", "Tampilkan Laporan Filter", "Buat Laporan", "Update Status", "Hapus Laporan", "Logout"],
                pointer="👉"
            ).execute()
            clear()
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
        print(colored("=== DAFTAR LAPORAN ===", "cyan"))
        if not laporan:
            print(colored("Belum Ada Laporan.", "red"))
            pause()
            clear()
            return

        headers = ["ID", "Lokasi", "Jenis", "Status", "Deskripsi", "Tanggal", "User"]
        rows = [
            [id, data["lokasi"], data["jenis"], data["status"],
            data["deskripsi"], log_status.get(id, "Belum ada"), data["User"]]
            for id, data in laporan.items()
        ]
        print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
        input("\nTekan Enter")
        clear()
    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()


def FILTER_READ():
    clear()
    try:
        print(colored("=== FILTER LAPORAN BERDASARKAN STATUS ===", "cyan"))
        status_filter = inquirer.select(
            message="Pilih Status Laporan yang Ingin Ditampilkan:",
            choices=["Belum Ditindak", "Diproses", "Sudah Ditindak"],
            pointer="👉"
        ).execute()

        filtered = {
            id: data for id, data in laporan.items()
            if data["status"] == status_filter
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
        print(colored("=== CREATE LAPORAN ===", "cyan"))
        lokasi = input("Lokasi kejadian: ").strip()
        if not lokasi:
            raise ValueError(colored("Lokasi Tidak Boleh Kosong.", "red"))

        jenis = inquirer.select(
            message="Pilih Jenis Masalah:",
            choices=["Sampah", "Pencemaran", "Perusakan"],
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
            "status": "Belum Ditindak",
            "User": username
        }
        log_status[id] = timestamp()

        print(colored("Laporan Telah Berhasil Dibuat.", "green"))
        pause()
        clear()

    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()
        clear()

def UPDATE():
    clear()
    try:
        print(colored("=== UPDATE STATUS LAPORAN ===", "cyan"))
        id = input("Masukkan ID Laporan: ").strip()
        if id not in laporan:
            raise ValueError(colored("ID Tidak Ditemukan.", "red"))

        status_baru = inquirer.select(
            message="Pilih Status Baru:",
            choices=["Belum Ditindak", "Diproses", "Sudah Ditindak"],
            pointer="👉"
        ).execute()

        laporan[id]["status"] = status_baru
        log_status[id] = timestamp()

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
        print(colored("=== HAPUS LAPORAN ===", "red"))
        id = input("Masukkan ID Laporan: ").strip()
        if id not in laporan:
            raise ValueError("ID Tidak Ditemukan.")

        konfirmasi = inquirer.confirm("Apakah Anda Yakin Ingin Menghapus Laporan Ini?", default=False).execute()
        if konfirmasi:
            del laporan[id]
            log_status.pop(id, None)
            print(colored("Laporan Dihapus.", "red"))
        else:
            print(colored("Dibatalkan.", "yellow"))
        pause()
        clear()

    except Exception as e:
        print(colored(f"\nError: {e}", "red"))
        pause()
        clear()
