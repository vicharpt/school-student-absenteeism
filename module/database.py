import os
import sys
sys.path.append(os.getcwd())

from data import siswa
from configparser import ConfigParser

config = ConfigParser()
config.read("module/config/config.conf")

database = {
    "key": config["options"]["key"] if config["options"]["key"] else "admin",
    "information_status_symbol": {
        "hadir": config["information status symbol"]["hadir"],
        "izin": config["information status symbol"]["izin"],
        "sakit": config["information status symbol"]["sakit"],
        "alpha": config["information status symbol"]["alpha"],
    },
    "show_status_code": bool(int(config["options"]["show_status_code"])),
    "class": config["class"]["class"],
    "teacher": config["class"]["teacher"],
    "siswa": siswa.siswa,
    "date": {
        "year": config["date"]["year"],
        "month": config["date"]["month"],
        "day": config["date"]["day"]
    },
}

