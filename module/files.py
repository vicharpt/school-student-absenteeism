import os
from glob import glob
from copy import deepcopy

from .code import shift
from .database import database
from .display import status_code, loading_and_clear

def file_action(date, mode="", data=""):
    file_name = f"{date['year']}-{date['month']}"
    with open(f"database/{date['year']}/{date['month']}/{file_name}.txt", mode) as file:
        data =  file.write(f"{data}\n") if mode == "a" else file.readlines()
    
    data_dict = {}
    if mode == "r":
        for line in data:
            data_raw = list(shift(line , database["key"], to="left"))
            data_raw.pop()
            data_raw = "".join(data_raw).split("|")
            data_date = data_raw[0].replace(",","_")
            data_dict[data_date] = data_raw[1].split(",")

        return [date["year"],date["month"],date["day"]], data_dict[f"{date['year']}_{date['month']}_{date['day']}"]

def create(data, date):
    os.makedirs("database", exist_ok=True)
    os.makedirs(f"database/{date['year']}", exist_ok=True)
    os.makedirs(f"database/{date['year']}/{date['month']}", exist_ok=True)

    file_action(date, mode="a", data=data)
    
    if database["information_success"]:
        status_code("creating", f"{date['year']}/{date['month']}/{date['day']}")

def read(date):
    try:
        data_date, data = file_action(date, mode="r")
        date = {
            "year": data_date[0],
            "month": data_date[1],
            "day": data_date[2]
        }
        
        siswa = deepcopy(database["siswa"])
        for i, status in enumerate(siswa):
            status["status"] = data[i]
        return data_date, siswa
    except:
        return [date["year"], date["month"], date["day"],], ""

get_year = lambda: [year for year in os.listdir(f"{os.getcwd()}/database") if not "." in year]

get_month = lambda year: [month for month in os.listdir(f"{os.getcwd()}/database/{year}") if not "." in month]

def get_day():
    data = file_action()