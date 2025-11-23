import os
from InquirerPy import inquirer
from loginregis import login, register
from admin import MENU_ADMIN
from manager import MENU_MANAGER
from user import MENU_USER
from data import load_dummy

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_input(pesan, opsi):
    clear()
    return inquirer.select(
        message=pesan,
        choices=opsi,
        pointer="👉",
        default=opsi[0]
    ).execute()
    

def main():
    load_dummy()
    while True:
        try:
            pilihan = menu_input("===== >>> [MENU UTAMA] <<< =====", ["Login", "Register", "Keluar"])

            if pilihan == "Register":
                clear()
                register()

            elif pilihan == "Login":
                clear()
                username, role = login()
                if not username:
                    continue

                if role == "manager":
                    MENU_MANAGER()
                elif role == "admin":
                    MENU_ADMIN(username)
                elif role == "user":
                    MENU_USER(username)

                else:
                    print("Anda Heker, ga boleh masuk.")
                    input("Tekan Enter")

            elif pilihan == "Keluar":
                clear()
                print("Terima kasih telah menggunakan aplikasi.")
                break

        except Exception as e:
            print(f"\nError: {e}")
            input("\nTekan Enter")

if __name__ == "__main__":
    main()
