import os
from InquirerPy import inquirer
from prettytable import PrettyTable
from data import users

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MENU_MANAGER():
    while True:
        try:
            menu = inquirer.select(
                message="=== >>> [Menu Manager] <<< ===",
                choices=["Tampilkan semua akun", "Tampilkan akun filter", "Buat akun", "Update akun", "Hapus akun", "Logout"],
                pointer="👉"
            ).execute()
            
            clear()
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
    print("=== DAFTAR AKUN ===")
    table = PrettyTable()
    table.field_names = ["Username", "Password", "Role"]
    for username, info in users.items():
        table.add_row([username, info["password"], info["role"]])
    print(table)
    input("\nTekan Enter")

def READ_FILTER_ACC():
    clear()
    try:
        print("=== FILTER AKUN BERDASARKAN ROLE ===")
        role_filter = inquirer.select(
            message="Pilih role yang ingin ditampilkan:",
            choices=["admin", "user", "manager"],
            pointer="👉"
        ).execute()

        filtered = {
            username: info for username, info in users.items()
            if info["role"] == role_filter
        }

        if not filtered:
            print(f"Tidak ada akun dengan role '{role_filter}'.")
        else:
            table = PrettyTable()
            table.field_names = ["Username", "Password", "Role"]
            for username, info in filtered.items():
                table.add_row([username, info["password"], info["role"]])
            print(table)

        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def CREATE_ACC():
    clear()
    try:
        print("=== BUAT AKUN BARU ===")
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
        print("=== UBAH AKUN ===")
        username = input("Username yang ingin diubah: ").strip()
        if username not in users:
            raise ValueError("Username tidak ditemukan.")

        pilihan = inquirer.select(
            message="Apa yang ingin Anda ubah?",
            choices=["Password", "Role"],
            pointer="👉"
        ).execute()

        if pilihan == "Password":
            new_password = input("Password baru (min 6 karakter): ").strip()
            if len(new_password) < 6:
                raise ValueError("Password terlalu pendek.")
            users[username]["password"] = new_password
            print("Password berhasil diubah.")

        elif pilihan == "Role":
            new_role = inquirer.select(
                message="Pilih role baru:",
                choices=["admin", "user", "manager"],
                pointer="👉"
            ).execute()
            users[username]["role"] = new_role
            print("Role berhasil diubah.")

        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def DELETE_ACC():
    clear()
    try:
        print("=== HAPUS AKUN ===")
        username = input("Username yang ingin dihapus: ").strip()
        if username not in users:
            raise ValueError("Username tidak ditemukan.")
        if username == "admin":
            raise ValueError("Akun admin tidak boleh dihapus.")

        konfirmasi = inquirer.confirm("Yakin ingin menghapus akun ini?", default=False).execute()
        if konfirmasi:
            del users[username]
            print("Akun berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
