import os
from InquirerPy import inquirer
from loginregis import login, register
from admin import tampilkan_laporan, buat_laporan, update_laporan, hapus_laporan
from user import menu_user

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

                if role == "admin":
                    while True:
                        try:
                            menu = menu_input("=== >>> [MENU ADMIN] <<< ===", [
                                "Tampilkan laporan", "Buat laporan", "Update status", "Hapus laporan", "Logout"
                            ])
                            clear()
                            if menu == "Tampilkan laporan":
                                tampilkan_laporan()
                            elif menu == "Buat laporan":
                                buat_laporan(username)
                            elif menu == "Update status":
                                update_laporan()
                            elif menu == "Hapus laporan":
                                hapus_laporan()
                            elif menu == "Logout":
                                break
                        except Exception as e:
                            print(f"\nError: {e}")
                            input("\nTekan Enter")

                elif role == "user":
                    menu_user(username)

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
