import os
import sys
sys.path.append(os.getcwd())

from data import siswa
from configparser import ConfigParser

config = ConfigParser()
config.read("module/config/config.conf")

database = {
    "key": config["options"]["key"] if config["options"]["key"] else "default",
    "show_status_code": bool(int(config["options"]["show_status_code"])),
    "class": config["class"]["class"],
    "siswa": siswa.siswa,
    "date": {
        "year": config["date"]["year"],
        "month": config["date"]["month"],
        "day": config["date"]["day"]
    },
}

