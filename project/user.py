import os
from InquirerPy import inquirer
from admin import buat_laporan, tampilkan_laporan

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_user(username):
    while True:
        try:
            clear()
            pilihan = inquirer.select(
                message="=== [Menu Pengguna] ===",
                choices=["Buat laporan", "Tampilkan laporan", "Logout"],
                pointer="👉"
            ).execute()

            clear()
            if pilihan == "Buat laporan":
                buat_laporan(username)
            elif pilihan == "Tampilkan laporan":
                tampilkan_laporan()
            elif pilihan == "Logout":
                break
        except Exception as e:
            print(f"\nError: {e}")
            input("\nTekan Enter")
