from peewee import fn

from models import Notice


def save_notices(updated_notices):
    Notice.insert_many(updated_notices).execute()


def get_latest_id():
    query = Notice.select(fn.MAX(Notice.notice_id))
    latest_id = query if query.scalar() else 0
    return latest_id
