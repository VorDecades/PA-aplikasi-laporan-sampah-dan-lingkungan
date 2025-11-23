import os
from InquirerPy import inquirer
from tabulate import tabulate
from data import laporan, log_status, timestamp

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MENU_ADMIN(username):
    clear()
    while True:
        try:
            menu = inquirer.select(
                message="\n============================\n=== >>> [Menu Admin] <<< ===\n============================",
                choices=["Tampilkan semua laporan", "Tampilkan Laporan Filter", "Buat laporan", "Update status", "Hapus laporan", "Logout"],
                pointer="👉"
            ).execute()
            clear()
            if menu == "Tampilkan semua laporan":
                                READ()
            elif menu == "Tampilkan Laporan Filter":
                                FILTER_READ()
            elif menu == "Buat laporan":
                                CREATE(username)
            elif menu == "Update status":
                                UPDATE()
            elif menu == "Hapus laporan":
                                DELETE()
            elif menu == "Logout":
                                break
        except Exception as e:
            print(f"\nError: {e}")
            input("\nTekan Enter")

def READ():
    clear()
    try:
        print("=== DAFTAR LAPORAN ===")
        if not laporan:
            print("Belum ada laporan.")
            input("\nTekan Enter")
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
        print(f"\nError: {e}")
        input("\nTekan Enter")
        clear()

def FILTER_READ():
    clear()
    try:
        print("=== FILTER LAPORAN BERDASARKAN STATUS ===")
        status_filter = inquirer.select(
            message="Pilih status laporan yang ingin ditampilkan:",
            choices=["belum ditindak", "di proses", "sudah ditindak"],
            pointer="👉"
        ).execute()

        # ambil hanya laporan sesuai status
        filtered = {
            id: data for id, data in laporan.items()
            if data["status"] == status_filter
        }

        if not filtered:
            print(f"Tidak ada laporan dengan status '{status_filter}'.")
        else:
            headers = ["ID", "Lokasi", "Jenis", "Status", "Deskripsi", "Tanggal", "User"] # header
            rows = [
                [id, data["lokasi"], data["jenis"], data["status"],
                 data["deskripsi"], log_status.get(id, "Belum ada"), data["User"]] # isi data
                for id, data in filtered.items()   # munculkan semua data sesuai filter
            ]
            print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))  
        input("\nTekan Enter")
        clear()

    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
        clear()


def CREATE(username):
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
            "User": username
        }
        log_status[id] = timestamp()
        print("Laporan berhasil dibuat.")
        input("\nTekan Enter")
        clear()

    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
        clear()

def UPDATE():
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
        clear()

    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
        clear()

def DELETE():
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
        clear()

    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
        clear()