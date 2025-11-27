import os
from data import log_activity
from InquirerPy import inquirer
from termcolor import colored
from tabulate import tabulate
from data import users
from activity import MENU_ACTIVITY

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

# AJIS
def MENU_MANAGER(username):
    while True:
        try:
            clear()
            width = 45  
            print(colored("\033[1m" + "\n" + "=" * width, "yellow"))
            print(colored("[ MENU MANAGER ]".center(width), "yellow"))
            print(colored("=" * width + "\033[0m", "yellow"))
            print(colored(f"\nSELAMAT DATANG {username}\n", "cyan"))
            menu = inquirer.select(
                message="pilih menu yang ingin diakses: ",
                choices=[
                    "Activity",
                    "Tampilkan Semua Akun",
                    "Tampilkan Akun Filter",
                    "Buat Akun",
                    "Update Akun",
                    "Hapus Akun",
                    "Logout"
                ],
                pointer="👉",
                qmark=""
            ).execute()
            
            if menu == "Activity":
                MENU_ACTIVITY()
            elif menu == "Tampilkan Semua Akun":
                READ_ACC()
            elif menu == "Tampilkan Akun Filter":
                READ_FILTER_ACC()
            elif menu == "Buat Akun":
                CREATE_ACC()
            elif menu == "Update Akun":
                UPDATE_ACC()
            elif menu == "Hapus Akun":
                DELETE_ACC()
            elif menu == "Logout":
                break
        except Exception as e:
            print(f"\nError: {e}")
            pause()

#AFIF
def READ_ACC():
    clear()
    try:
        print(colored("==================================================", "yellow"))
        print(colored("              DAFTAR SEMUA AKUN                   ", "yellow"))
        print(colored("==================================================", "yellow"))
        
        headers = ["Username", "Password", "Role"]
        rows = []
        
        for username in users:
            password = users[username]["password"]
            role = users[username]["role"]
            rows.append([username, password, role])
        
        print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
        pause()
        clear()
        
    except Exception as e:
        print(colored(f"\nTerjadi kesalahan: {e}", "red"))
        pause()
        clear()

def READ_FILTER_ACC():
    clear()
    try:
        print(colored("==================================================", "yellow"))
        print(colored("        FILTER AKUN BERDASARKAN ROLE              ", "yellow"))
        print(colored("==================================================", "yellow"))
        
        role_filter = inquirer.select(
            message="Pilih Role:",
            choices=["admin", "user", "manager"],
            pointer="👉",
            qmark=""
        ).execute()

        clear()
        print(colored("==================================================", "yellow"))
        print(colored("        AKUN DENGAN ROLE: " + role_filter.upper() + "              ", "yellow"))
        print(colored("==================================================", "yellow"))
        
        headers = ["Username", "Password", "Role"]
        rows = []
        
        for username in users:
            if users[username]["role"] == role_filter:
                password = users[username]["password"]
                role = users[username]["role"]
                rows.append([username, password, role])

        if len(rows) == 0:
            print(colored(f"\nTidak ada akun dengan role '{role_filter}'", "yellow"))
        else:
            print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

        pause()
        clear()
        
    except Exception as e:
        print(colored(f"\nTerjadi kesalahan: {e}", "red"))
        pause()
        clear()

def CREATE_ACC():
    clear()
    try:
        print(colored("==================================================", "yellow"))
        print(colored("              BUAT AKUN BARU                      ", "yellow"))
        print(colored("==================================================", "yellow"))

        username = input("\nUsername baru: ")
        password = input("Password (minimal 6 karakter): ")

        if username == "" or password == "":
            print(colored("\nUsername dan password tidak boleh kosong", "red"))
            pause()
            clear()
            return
        
        if len(password) < 6:
            print(colored("\nPassword terlalu pendek, minimal 6 karakter", "red"))
            pause()
            clear()
            return
        
        if username in users:
            print(colored("\nUsername sudah terdaftar", "red"))
            pause()
            clear()
            return

        role = inquirer.select(
            message="Pilih Role:",
            choices=["admin", "user", "manager"],
            pointer="👉",
            qmark=""
        ).execute()

        users[username] = {"password": password, "role": role}
        print(colored("\nAkun berhasil dibuat", "green"))
        pause()
        clear()
        
    except Exception as e:
        print(colored(f"\nTerjadi kesalahan: {e}", "red"))
        pause()
        clear()

def UPDATE_ACC():
    clear()
    try:
        print(colored("==================================================", "yellow"))
        print(colored("              UPDATE AKUN                         ", "yellow"))
        print(colored("==================================================", "yellow"))

        username = input("\nMasukkan username yang ingin diubah: ")
        
        if username not in users:
            print(colored("\nUsername tidak ditemukan", "red"))
            pause()
            clear()
            return

        pilihan = inquirer.select(
            message="Apa yang ingin diubah?",
            choices=["Password", "Role"],
            pointer="👉",
            qmark=""
        ).execute()

        if pilihan == "Password":
            password_lama = users[username]["password"]
            password_baru = input("\nMasukkan password baru (minimal 6 karakter): ")
            
            if len(password_baru) < 6:
                print(colored("\nPassword terlalu pendek, minimal 6 karakter", "red"))
                pause()
                clear()
                return
            
            if password_baru == password_lama:
                print(colored("\nPassword baru tidak boleh sama dengan password lama", "red"))
                pause()
                clear()
                return
            
            users[username]["password"] = password_baru
            print(colored("\nPassword berhasil diubah", "green"))

        elif pilihan == "Role":
            role_lama = users[username]["role"]
            print(f"\nRole saat ini: {role_lama}")
            
            role_baru = inquirer.select(
                message="Pilih role baru:",
                choices=["admin", "user", "manager"],
                pointer="👉",
                qmark=""
            ).execute()
            
            if role_baru == role_lama:
                print(colored("\nRole baru tidak boleh sama dengan role lama", "red"))
                pause()
                clear()
                return
            
            users[username]["role"] = role_baru
            print(colored("\nRole berhasil diubah", "green"))

        pause()
        clear()
        
    except Exception as e:
        print(colored(f"\nTerjadi kesalahan: {e}", "red"))
        pause()
        clear()

def DELETE_ACC():
    clear()
    try:
        print(colored("==================================================", "yellow"))
        print(colored("              HAPUS AKUN                          ", "yellow"))
        print(colored("==================================================", "yellow"))

        username = input("\nMasukkan username yang ingin dihapus: ")
        
        if username not in users:
            print(colored("\nUsername tidak ditemukan", "red"))
            pause()
            clear()
            return
        
        if username == "admin":
            print(colored("\nAkun admin tidak boleh dihapus", "red"))
            pause()
            clear()
            return

        konfirmasi = inquirer.confirm(
            message=f"Yakin ingin menghapus akun '{username}'?",
            default=False,
            qmark=""
        ).execute()

        if konfirmasi == True:
            del users[username]
            print(colored("\nAkun berhasil dihapus", "green"))
        else:
            print(colored("\nPenghapusan dibatalkan", "yellow"))

        pause()
        clear()
        
    except Exception as e:
        print(colored(f"\nTerjadi kesalahan: {e}", "red"))
        pause()
        clear()