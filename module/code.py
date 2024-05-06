from string import ascii_letters, digits
from .database import database

chars = digits + ascii_letters + "\|/,.-^ "

def shift(data, key, to=""):
    result = ""
    k = 0
    for char in data:
        if k%len(key) == 0: k = 0
        index = eval(f"({chars.find(char)} {'+' if to == 'right' else '-'} {chars.find(key[k])}) % {len(chars)}")
        result += chars[index]
        k+=1
    return result

def format_status(status):
    information_status_symbol = database["information_status_symbol"]
    if status == "" or status == "1":
        status = information_status_symbol["hadir"]
    elif status == "2":
        status = information_status_symbol["izin"]
    elif status == "3":
        status = information_status_symbol["sakit"]
    elif status == "4":
        status = information_status_symbol["alpha"]
    else:
        status = "?"
    return status