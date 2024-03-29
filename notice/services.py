from datetime import datetime, timedelta

from peewee import fn

from logger import logger
from notice.models import Notice


def save_notices(updated_notices):
    Notice.insert_many(updated_notices).execute()
    logger.info(f"{len(updated_notices)}개의 공지가 데이터베이스에 저장되었습니다.")


def delete_old_notices():
    to_delete = Notice.delete().where(
        Notice.registered_at < datetime.now() - timedelta(weeks=12)
    )
    num_deleted = to_delete.execute()
    logger.info(f"{num_deleted}개의 공지가 데이터베이스에서 삭제되었습니다.")


def get_latest_id():
    query = Notice.select(fn.MAX(Notice.notice_id)).scalar()
    latest_id = query if query else 0
    return latest_id
