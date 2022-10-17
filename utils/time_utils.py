from datetime import datetime


def get_current_date():
    return datetime.today().strftime("%Y년 %m월 %d일")
