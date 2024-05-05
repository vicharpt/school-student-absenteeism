import os
from glob import glob
from copy import deepcopy

from .code import shift
from .database import database
from .display import status_code, loading_and_clear

def file_action(date, mode="", data=""):
    date_data = {}
    file_name = f"{date['year']}-{date['month']}"
    with open(f"database/{date['year']}/{date['month']}/{file_name}.txt", mode) as file:
        data =  file.write(data+"\n") if mode == "a" else file.readlines()
    
    if mode == "r":
        for line in data:
            k = f"{file_name.replace('-','_')}_{date['day']}"
            if not k in date_data:
                date_data[k] = data = shift(line , database["key"], to="left").replace("\n","")
    # if mode == "r" and "-^" in data:
    #     data = data.split("-^")
    return date_data

def create(data, date):
    os.makedirs("database", exist_ok=True)
    os.makedirs(f"database/{date['year']}", exist_ok=True)
    os.makedirs(f"database/{date['year']}/{date['month']}", exist_ok=True)

    file_action(date, mode="a", data=data)
    
    if database["show_status_code"]:
        status_code("creating", f"{date['year']}/{date['month']}/{date['day']}")

def read(date):
    try:
        data = file_action(date, mode="r")
        print(data)
        exit()
        data_date = data[0].split(",")
        data_date = {
            "year": data_date[0],
            "month": data_date[1],
            "day": data_date[2]
        }
        del data[0]
        status_siswa = data[0].split(",")
        del data
        
        siswa = deepcopy(database["siswa"])
        for i, data in enumerate(siswa):
            data["status"] = status_siswa[i]
        return data_date, siswa
    except:
        return date, ""

get_year = lambda: [year for year in os.listdir(f"{os.getcwd()}/database") if not "." in year]

get_month = lambda year: [month for month in os.listdir(f"{os.getcwd()}/database/{year}") if not "." in month]

def get_day():
    data = file_action()