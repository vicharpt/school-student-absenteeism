from datetime import datetime
from .database import database

now = datetime.now()

date = {
    "year": database["date"]["year"] if database["date"]["year"] else now.strftime("%Y"),
    "month": database["date"]["month"] if database["date"]["month"] else now.strftime("%m"),
    "day": database["date"]["day"] if database["date"]["day"] else now.strftime("%d"),
}
