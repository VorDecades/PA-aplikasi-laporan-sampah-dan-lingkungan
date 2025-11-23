import os
from data import users
from InquirerPy import inquirer
from admin import CREATE, READ, FILTER_READ

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MENU_USER(username):
    clear()
    while True:
        try:
            menu = inquirer.select(
                message="\n===============================\n=== >>> [Menu Pengguna] <<< ===\n===============================",
                choices=["Buat laporan", "Tampilkan semua laporan", "Tampilkan laporan Filter", "Ubah profil", "Logout"],
                pointer="👉"
            ).execute()

            clear()
            if menu == "Buat laporan":
                CREATE(username)
            elif menu == "Tampilkan semua laporan":
                READ()
            elif menu == "Tampilkan laporan Filter":
                FILTER_READ()
            elif menu == "Ubah profil":
                UPDATE_PROFILE()
            elif menu == "Logout":
                break
        except Exception as e:
            print(f"\nError: {e}")
            input("\nTekan Enter")
            clear()

def UPDATE_PROFILE():
    clear()
    try:
        print("=== UBAH PROFIL ===")
        username = input("Masukkan username saat ini: ").strip()
        password = input("Masukkan password saat ini: ").strip()

        # Validasi kredensial
        if username not in users or users[username]["password"] != password:
            raise ValueError("Username atau password salah.")

        pilihan = inquirer.select(
            message="Apa yang ingin Anda ubah?",
            choices=["Username", "Password"],
            pointer="→"
        ).execute()

        if pilihan == "Username":
            new_username = input("Masukkan username baru: ").strip()
            if not new_username:
                raise ValueError("Username baru tidak boleh kosong.")
            if new_username in users:
                raise ValueError("Username sudah digunakan.")
            users[new_username] = users.pop(username)
            print("Username berhasil diubah.")

        elif pilihan == "Password":
            new_password = input("Masukkan password baru (min 6 karakter): ").strip()
            if len(new_password) < 6:
                raise ValueError("Password terlalu pendek.")
            users[username]["password"] = new_password
            print("Password berhasil diubah.")

        input("\nTekan Enter")
        clear()

    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
        clear()
