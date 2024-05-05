from string import ascii_letters, digits

chars = digits + ascii_letters + "|/,.-^ "

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
    if status == "" or status == "1":
        status = "hadir"
    elif status == "2":
        status = "izin"
    elif status == "3":
        status = "sakit"
    elif status == "4":
        status = "alpha"
    else:
        status = "?"
    return status