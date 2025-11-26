# AJIS
import os
from InquirerPy import inquirer
from loginregis import login, register
from admin import MENU_ADMIN
from manager import MENU_MANAGER
from user import MENU_USER
from data import load_dummy
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))
    
def utama():
    clear()
    load_dummy()
    while True:
        try:
            clear()
            width = 45  # panjang garis
            print(colored("\n" + "=" * width, "yellow"))
            print(colored("[ SELAMAT DATANG ]".center(width), "yellow"))
            print(colored("[ APLIKASI PELAPORAN SAMPAH ]".center(width), "yellow"))
            print(colored("[ DAN LINGKUNGAN ]".center(width), "yellow"))
            print(colored("=" * width, "yellow"))
            pilihan = inquirer.select(
                message="pilih menu yang ingin diakses: ",
                choices=[
                    "Login",
                    "Register",
                    "Keluar"
                ],
                pointer="👉",
                qmark=""
            ).execute()

            if pilihan == "Register":
                clear()
                register()

            elif pilihan == "Login":
                clear()
                username, role = login()
                if not username:
                    continue

                if role == "manager":
                    MENU_MANAGER(username)
                elif role == "admin":
                    MENU_ADMIN(username)
                elif role == "user":
                    MENU_USER(username)
                else:
                    print("Anda Heker, ga boleh masuk.")
                    pause()
                    clear()

            elif pilihan == "Keluar":
                clear()
                print("Terima Kasih Telah Menggunakan Aplikasi.")
                break

        except Exception as e:
            print(f"\nError: {e}")
            pause()
            clear()

if __name__ == "__main__":
    utama()
