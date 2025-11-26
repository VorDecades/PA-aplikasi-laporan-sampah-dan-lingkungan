import os
from data import log_activity
from InquirerPy import inquirer
from termcolor import colored
from tabulate import tabulate
from data import users
from activity import MENU_ACTIVITY

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

# AJIS
def MENU_MANAGER(username):
    while True:
        try:
            clear()
            print(colored("\033[1m" + "\n" + "=" * 36 + "\n" + "====== >>> [Menu Manager] <<< ======" + "\n" + "=" * 36 + "\033[0m", "yellow"))
            print(colored(f"\nSELAMAT DATANG {username}", "cyan"))
            menu = inquirer.select(
                message="pilih menu yang ingin diakses: ",
                choices=[
                    "Activity",
                    "Tampilkan Semua Akun",
                    "Tampilkan Akun Filter",
                    "Buat Akun",
                    "Update Akun",
                    "Hapus Akun",
                    "Logout"
                ],
                pointer="👉"
            ).execute()
            
            if menu == "Activity":
                MENU_ACTIVITY()
            elif menu == "Tampilkan Semua Akun":
                READ_ACC()
            elif menu == "Tampilkan Akun Filter":
                READ_FILTER_ACC()
            elif menu == "Buat Akun":
                CREATE_ACC()
            elif menu == "Update Akun":
                UPDATE_ACC()
            elif menu == "Hapus Akun":
                DELETE_ACC()
            elif menu == "Logout":
                break
        except Exception as e:
            print(f"\nError: {e}")
            pause()

#AFIF
def READ_ACC():
    clear()
    headers = ["Username", "Password", "Role"]
    rows = [[username, info["password"], info["role"]] for username, info in users.items()]
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
    pause()

def READ_FILTER_ACC():
    clear()
    try:
        role_filter = inquirer.select(
            message="Pilih Role yang Ingin Ditampilkan:",
            choices=["admin", "user", "manager"],
            pointer="👉"
        ).execute()

        filtered = {u: info for u, info in users.items() if info["role"] == role_filter}

        if not filtered:
            print(colored(f"Tidak Ada Akun dengan Role '{role_filter}'.", "yellow"))
        else:
            headers = ["Username", "Password", "Role"]
            rows = [[u, info["password"], info["role"]] for u, info in filtered.items()]
            print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

        pause()
    except Exception as e:
        print(f"\nError: {e}")
        pause()

def CREATE_ACC():
    clear()
    try:
        username = input("Username Baru: ").strip()
        password = input("Password (min 6 karakter): ").strip()

        if not username or not password:
            raise ValueError(colored("Username dan Password Tidak Boleh Kosong.", "red"))
        if len(password) < 6:
            raise ValueError(colored("Password Terlalu Pendek.", "red"))
        if username in users:
            raise ValueError(colored("Username Sudah Terdaftar.", "red"))

        role = inquirer.select(
            message="Pilih Role Untuk Akun Baru:",
            choices=["admin", "user", "manager"],
            pointer="👉"
        ).execute()

        users[username] = {"password": password, "role": role}
        print(colored("Akun Berhasil Dibuat.", "green"))
        pause()
    except Exception as e:
        print(f"\nError: {e}")
        pause()

def UPDATE_ACC():
    clear()
    try:
        username = input(colored("Masukkan Username yang Ingin Diubah: ", "cyan")).strip()
        if username not in users:
            raise ValueError(colored("Username Tidak Ditemukan.", "red"))

        pilihan = inquirer.select(
            message="Apa yang Ingin Diubah?",
            choices=["Password", "Role"],
            pointer="👉"
        ).execute()

        if pilihan == "Password":
            current_password = users[username]["password"]
            new_password = input("Masukkan Password Baru (min 6 karakter): ").strip()

            if len(new_password) < 6:
                raise ValueError(colored("Password Terlalu Pendek.", "red"))
            if new_password == current_password:
                raise ValueError(colored("Password Baru Tidak Boleh Sama dengan Password Lama.", "red"))

            users[username]["password"] = new_password
            print(colored("\nPassword Berhasil Diubah.", "green"))

        elif pilihan == "Role":
            current_role = users[username]["role"]
            new_role = inquirer.select(
                message=f"Role Saat Ini: {current_role}. Pilih Role Baru:",
                choices=["admin", "user", "manager"],
                pointer="👉"
            ).execute()

            if new_role == current_role:
                raise ValueError(colored("Role Baru Tidak Boleh Sama dengan Role Lama.", "red"))

            users[username]["role"] = new_role
            print(colored("\nRole Berhasil Diubah.", "green"))
        pause()

    except Exception as e:
        print(f"\nError: {e}")
        pause()


def DELETE_ACC():
    clear()
    try:
        username = input(colored("Masukkan Username yang Ingin Dihapus: ", "cyan")).strip()
        if username not in users:
            raise ValueError(colored("Username Tidak Ditemukan.", "red"))
        if username == "admin":
            raise ValueError(colored("Akun Admin Tidak Boleh Dihapus.", "red"))

        konfirmasi = inquirer.confirm(
            message=f"Yakin Ingin Menghapus Akun '{username}'?",
            default=False
        ).execute()

        if konfirmasi:
            del users[username]
            print(colored("\nAkun Berhasil Dihapus.", "green"))
        else:
            print(colored("\nPenghapusan Dibatalkan.", "yellow"))
        pause()

    except Exception as e:
        print(f"\nError: {e}")
        pause()