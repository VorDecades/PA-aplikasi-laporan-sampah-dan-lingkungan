import os
from InquirerPy import inquirer
from tabulate import tabulate
from data import users

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MENU_MANAGER():
    while True:
        try:
            clear()
            menu = inquirer.select(
                message="=== >>> [Menu Manager] <<< ===",
                choices=[
                    "Tampilkan semua akun",
                    "Tampilkan akun filter",
                    "Buat akun",
                    "Update akun",
                    "Hapus akun",
                    "Logout"
                ],
                pointer="👉"
            ).execute()
            
            if menu == "Tampilkan semua akun":
                READ_ACC()
            elif menu == "Tampilkan akun filter":
                READ_FILTER_ACC()
            elif menu == "Buat akun":
                CREATE_ACC()
            elif menu == "Update akun":
                UPDATE_ACC()
            elif menu == "Hapus akun":
                DELETE_ACC()
            elif menu == "Logout":
                break
        except Exception as e:
            print(f"\nError: {e}")
            input("\nTekan Enter")

def READ_ACC():
    clear()
    headers = ["Username", "Password", "Role"]
    rows = [[username, info["password"], info["role"]] for username, info in users.items()]
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
    input("\nTekan Enter")

def READ_FILTER_ACC():
    clear()
    try:
        role_filter = inquirer.select(
            message="Pilih role yang ingin ditampilkan:",
            choices=["admin", "user", "manager"],
            pointer="👉"
        ).execute()

        filtered = {u: info for u, info in users.items() if info["role"] == role_filter}

        if not filtered:
            print(f"Tidak ada akun dengan role '{role_filter}'.")
        else:
            headers = ["Username", "Password", "Role"]
            rows = [[u, info["password"], info["role"]] for u, info in filtered.items()]
            print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def CREATE_ACC():
    clear()
    try:
        username = input("Username baru: ").strip()
        password = input("Password (min 6 karakter): ").strip()

        if not username or not password:
            raise ValueError("Username dan password tidak boleh kosong.")
        if len(password) < 6:
            raise ValueError("Password terlalu pendek.")
        if username in users:
            raise ValueError("Username sudah terdaftar.")

        role = inquirer.select(
            message="Pilih role untuk akun baru:",
            choices=["admin", "user", "manager"],
            pointer="👉"
        ).execute()

        users[username] = {"password": password, "role": role}
        print("Akun berhasil dibuat.")
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def UPDATE_ACC():
    clear()
    try:
        username = input("Masukkan username yang ingin diubah: ").strip()
        if username not in users:
            raise ValueError("Username tidak ditemukan.")

        pilihan = inquirer.select(
            message="Apa yang ingin diubah?",
            choices=["Password", "Role"],
            pointer="👉"
        ).execute()

        if pilihan == "Password":
            new_password = input("Masukkan password baru (min 6 karakter): ").strip()
            if len(new_password) < 6:
                raise ValueError("Password terlalu pendek.")
            users[username]["password"] = new_password
            print("\nPassword berhasil diubah.")

        elif pilihan == "Role":
            new_role = inquirer.select(
                message="Pilih role baru:",
                choices=["admin", "user", "manager"],
                pointer="👉"
            ).execute()
            users[username]["role"] = new_role
            print("\nRole berhasil diubah.")

        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def DELETE_ACC():
    clear()
    try:
        username = input("Masukkan username yang ingin dihapus: ").strip()
        if username not in users:
            raise ValueError("Username tidak ditemukan.")
        if username == "admin":
            raise ValueError("Akun admin tidak boleh dihapus.")

        konfirmasi = inquirer.confirm(
            message=f"Yakin ingin menghapus akun '{username}'?",
            default=False
        ).execute()

        if konfirmasi:
            del users[username]
            print("\nAkun berhasil dihapus.")
        else:
            print("\nPenghapusan dibatalkan.")

        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")