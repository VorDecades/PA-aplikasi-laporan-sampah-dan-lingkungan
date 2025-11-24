import os
from termcolor import colored
from tabulate import tabulate
from InquirerPy import inquirer
from data import log_activity, report_activity

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(colored("\nTekan Enter", "grey"))

def MENU_ACTIVITY():
    while True:
        try:
            clear()
            print(colored("\033[1m" + "\n" + "=" * 36 + "\n" + "====== >>> [Activity] <<< ======" + "\n" + "=" * 36 + "\033[0m", "yellow"))
            pilihan = inquirer.select(
                message="pilih jenis aktivitas yang ingin ditampilkan: ",
                choices=["Log Login", "Pembuatan Laporan", "Update Laporan", "Hapus Laporan", "Kembali"],
                pointer="👉"
            ).execute()

            if pilihan == "Log Login":
                READ_LOG_ACTIVITY()
            elif pilihan == "Pembuatan Laporan":
                READ_REPORT_ACTIVITY("create")
            elif pilihan == "Update Laporan":
                READ_REPORT_ACTIVITY("update")
            elif pilihan == "Hapus Laporan":
                READ_REPORT_ACTIVITY("delete")
            elif pilihan == "Kembali":
                break
        except Exception as e:
            print(colored(f"\nError: {e}", "red"))
            pause()

def READ_LOG_ACTIVITY():
    clear()
    print(colored("=== LOG LOGIN ===", "cyan"))
    if not log_activity:
        print(colored("Belum ada aktivitas login.", "yellow"))
    else:
        headers = ["User", "Role", "Waktu Login"]
        rows = [[log["user"], log["role"], log["time"]] for log in log_activity]
        print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
    pause()

def READ_REPORT_ACTIVITY(filter_type):
    clear()
    if not report_activity:
        print(colored("Belum ada aktivitas laporan.", "yellow"))
        pause()
        return

    headers = ["ID", "Status Sebelum", "Status Sesudah", "Actor", "Waktu"]
    rows = []

    for log in report_activity:
        if filter_type == "create" and log["before"] is None:
            rows.append([log["id"], "-", log["after"], log["actor"], log["time"]])
        elif filter_type == "update" and log["before"] and log["after"]:
            rows.append([log["id"], log["before"], log["after"], log["actor"], log["time"]])
        elif filter_type == "delete" and log["after"] is None:
            rows.append([log["id"], log["before"], "di hapus", log["actor"], log["time"]])

    if not rows:
        print(colored("Tidak ada data untuk filter ini.", "yellow"))
    else:
        print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

    pause()
