import os
import inquirer
from data import users, log_activity, timestamp

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def register():
    clear()
    try:
        print("=== REGISTRASI ===")
        username = input("Username: ").strip()
        password = input("Password (min 6 karakter): ").strip()

        if not username or not password:
            raise ValueError("Username dan password tidak boleh kosong.")
        if len(password) < 6:
            raise ValueError("Password terlalu pendek.")
        elif username in users:
            raise ValueError("Username sudah terdaftar.")

        users[username] = {"password": password, "role": "user"}
        print("\nRegistrasi berhasil.")
        input("\nTekan Enter")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")

def login():
    clear()
    try:
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nLogin berhasil sebagai {role}")

            # simpan log activity
            log_activity.append({
                "user": username,
                "role": role,
                "time": timestamp()
            })

            input("\nTekan Enter")
            return username, role
        else:
            raise ValueError("Username atau password salah.")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nTekan Enter")
        return None, None