from peewee import fn

from notice.models import Notice


def save_notices(updated_notices):
    Notice.insert_many(updated_notices).execute()


def get_latest_id():
    query = Notice.select(fn.MAX(Notice.notice_id)).scalar()
    latest_id = query if query else 0
    return latest_id
