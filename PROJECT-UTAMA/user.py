# IHSAN
import os
from data import users
from InquirerPy import inquirer
from termcolor import colored
from admin import CREATE, READ, FILTER_READ

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

def MENU_USER(username):
    while True:
        try:
            clear()
            print(colored("\033[1m" + "\n" + "=" * 37 + "\n" + "====== >>> [Menu Pengguna] <<< ======" + "\n" + "=" * 37 + "\033[1m", "yellow"))
            print(colored(f"\nSELAMAT DATANG {username}\n", "cyan"))
            menu = inquirer.select(
                message="pilih menu yang ingin diakses: ",
                choices=["Buat Laporan", "Tampilkan Semua Laporan", "Tampilkan Laporan Filter", "Ubah Profil", "Logout"],
                pointer="👉",
                qmark=""
            ).execute()

            if menu == "Buat Laporan":
                CREATE(username)
            elif menu == "Tampilkan Semua Laporan":
                READ()
            elif menu == "Tampilkan Laporan Filter":
                FILTER_READ()
            elif menu == "Ubah Profil":
                UPDATE_PROFILE()
            elif menu == "Logout":
                break
        except Exception as e:
            print(f"\nError: {e}")
            pause()
            clear()

def UPDATE_PROFILE():
    clear()
    try:
        print(colored("\033[1m" + "\n" + "=" * 37 + "\n" + "====== >>> [Ubah Profil] <<< ======" + "\n" + "=" * 37 + "\033[0m", "yellow"))
        username = input("Masukkan Username Saat Ini: ").strip()
        password = input("Masukkan Password Saat Ini: ").strip()

        # Validasi kredensial
        if username not in users or users[username]["password"] != password:
            raise ValueError(colored("Username atau Password Salah.", "red"))

        pilihan = inquirer.select(
            message="Apa yang Ingin Anda Ubah?",
            choices=["Username", "Password"],
            pointer="👉",
            qmark=""
        ).execute()

        if pilihan == "Username":
            new_username = input("Masukkan Username Baru: ").strip()
            if not new_username:
                raise ValueError(colored("Username Baru Tidak Boleh Kosong.", "red"))
            if new_username in users:
                raise ValueError(colored("Username Sudah Digunakan.", "red"))
            users[new_username] = users.pop(username)
            print(colored("Username Berhasil Diubah.", "green"))

        elif pilihan == "Password":
            new_password = input("Masukkan Password Baru (min 6 karakter): ").strip()
            if len(new_password) < 6:
                raise ValueError(colored("Password Terlalu Pendek.", "red"))
            users[username]["password"] = new_password
            print(colored("Password Berhasil Diubah.", "green"))

        pause()
        clear()

    except Exception as e:
        print(f"\nError: {e}")
        pause()
        clear()
