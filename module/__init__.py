import os
import sys
sys.path.append(os.getcwd())

from .auth import auth
from .display import clear, banner, menu, loading_and_clear, table_absensi
from .runing_program import absensi, pantau_kehadiran
from .database import database
from .files import create, read
from .date import date

# auth(database["key"])