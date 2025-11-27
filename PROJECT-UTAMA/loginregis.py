import os
from termcolor import colored
from data import users, log_activity, timestamp

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

def register():
    clear()
    try:
        print(colored(
        "\033[1m"
        + "\n" + "=" * 32
        + "\n" + "====== >>> [REGISTER] <<< ======"
        + "\n" + "=" * 32
        + "\033[0m\n",
        "yellow"
        ))
        username = input("Username: ").strip()
        password = input("Password (min 6 karakter): ").strip()

        if not username or not password:
            raise ValueError("Username dan Password Tidak Boleh Kosong.")
        if len(password) < 6:
            raise ValueError(colored("Password Terlalu Pendek.", "red"))
        elif username in users:
            raise ValueError(colored("Username Sudah Terdaftar.", "red"))

        users[username] = {"password": password, "role": "user"}
        print(colored("\nRegistrasi berhasil.", "green"))
        pause()
    except Exception as e:
        print(f"\nError: {e}")
        pause()

def login():
    clear()
    try:
        print(colored(
        "\033[1m"                # aktifkan bold
        + "\n" + "=" * 29        # garis atas
        + "\n" + "====== >>> [LOGIN] <<< ======"  # judul menu
        + "\n" + "=" * 29        # garis bawah
        + "\033[0m\n",             # reset bold
        "yellow"                 # warna teks
        ))
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(colored(f"\nLogin Berhasil Sebagai {role}", "green"))

            # simpan log activity
            log_activity.append({
                "user": username,
                "role": role,
                "time": timestamp()
            })

            pause()
            return username, role
        else:
            raise ValueError(colored("Username atau Password Salah.", "red"))
    except Exception as e:
        print(f"\nError: {e}")
        pause()
        return None, None