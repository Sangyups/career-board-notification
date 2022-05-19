from datetime import datetime

from const import DATETIME_FORMAT
from services import save_notices, get_latest_id
from web_scraping import get_notices_from_career_board


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

    return updated_notices


if __name__ == "__main__":
    updated_notices = get_updated_notices()
    save_notices(updated_notices)
