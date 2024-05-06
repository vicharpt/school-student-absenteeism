from .display import banner, loading_and_clear
from.database import database

def auth(key):
    i = 1
    punishment = 2
    while True:
        banner(f"selamat datang {database['teacher']}")
        print(f"{'masukan kata sandi sebelum melanjutkan'.upper():^84}")
        print("="*84)
        auth = input("kata sandi >> ")
        if auth == key: break
        elif i == 3 or i%5 == 0:
            if i == 5: 
                i+=1
                continue
            punishment += 1
            loading_and_clear(f"{i} kali percobaan gagal silahkan tunggu dalam {punishment}", s=punishment)
        i+=1