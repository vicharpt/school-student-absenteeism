import os
from time import sleep

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def banner(title, clear_screen=True):
    if clear_screen: clear()
    print("="*84)
    print(f"{title.upper():^84}")
    print("="*84)

def menu(list, list_0):
    for i, m in enumerate(list, 1):
        print(f"{i}.{m.title()}")
    print(f"0.{list_0.title()}")
    print("-"*84)
    return int(input("Pilih >> "))

def loading_and_clear(text="", error=False, message="", s=2.5):
    print(f"Error : {message}" if error else text)
    sleep(s)
    clear()

def table_absensi(data):
    print(f"| {'No':<3}|{'Induk':^20}| {'Nama':<35}|{'L/P':^5}| {'Keterangan':^11} |")
    print("="*84)
    for i, dt in enumerate(data, 1):
        print(f"| {dt['no_absen']:<3}|{dt['induk']:^20}| {dt['name'].upper():<35}|{dt['gender'].upper():^5}| {dt['status'].upper():^11} |")
    print("="*84)

def status_code(message, path):
    print("="*84)
    print(f"Succesfully {message} code\nSource \t: database/{path}.txt")
    print("="*84)
    sleep(5)
    clear()