import os
import sys
sys.path.append(os.getcwd())

from data import siswa, perpustakan
from configparser import ConfigParser

config = ConfigParser()
config.read("module/config/config.conf")

database = {
    "auth": bool(int(config["options"]["auth"])),
    "key": config["options"]["key"] if config["options"]["key"] else "admin",
    "information_status_symbol": {
        "hadir": config["information_status_symbol"]["hadir"],
        "izin": config["information_status_symbol"]["izin"],
        "sakit": config["information_status_symbol"]["sakit"],
        "alpha": config["information_status_symbol"]["alpha"],
    },
    "show_status_code": bool(int(config["options"]["information_succes"])),
    "class": config["class"]["class"],
    "teacher": config["class"]["teacher"] if config["class"]["teacher"] else "!!!nama guru belum diatur!!!",
    "siswa": siswa.siswa,
    "date": {
        "year": config["date"]["year"],
        "month": config["date"]["month"],
        "day": config["date"]["day"]
    },
    "library": perpustakan.petunjuk
}

