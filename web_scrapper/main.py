from datetime import datetime

from const import DATETIME_FORMAT
from logger import logger
from notice.services import get_latest_id, save_notices
from notification.index import notify_notices
from web_scrapper import get_notices_from_career_board


def get_updated_notices():
    notices = get_notices_from_career_board()
    latest_id = get_latest_id()
    updated_notices = []
    for notice in notices:
        notice_id, title, manager, view_counts, registered_at, link = (
            int(notice[0]),
            notice[1],
            notice[2],
            int(notice[3]),
            datetime.strptime(notice[4], DATETIME_FORMAT).date(),
            notice[5],
        )
        if notice_id <= latest_id:
            break
        updated_notices.append(
            tuple([notice_id, title, manager, view_counts, registered_at, link])
        )
    logger.info(f"{len(updated_notices)}개의 새로운 공지를 가져왔습니다.")
    return updated_notices


if __name__ == "__main__":
    logger.info("알리미 실행")
    updated_notices = get_updated_notices()
    if updated_notices:
        notify_notices(updated_notices)
        save_notices(updated_notices)
