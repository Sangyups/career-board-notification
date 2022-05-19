from datetime import datetime

import requests
from bs4 import BeautifulSoup
from peewee import fn

from const import URL, URL_SUFFIX, DATETIME_FORMAT
from models import Notice


def get_text_from_element(element):
    return element.get_text().strip()


def get_notices():
    notice_list = []
    response = requests.get(URL + URL_SUFFIX)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    table_body = soup.select_one(
        "#jwxe_main_content > div > div > div > div.t_list.test20200330 > table > tbody"
    )
    rows = table_body.select("tr")
    for table_row in rows:
        cols = table_row.select("td")
        new_cols = list(map(get_text_from_element, cols))
        new_cols.append(URL + cols[1].select_one("a").attrs["href"])
        notice_list.append(new_cols)
        print(new_cols)

    return notice_list


def get_updated_notices(notices):
    query = Notice.select(fn.MAX(Notice.notice_id))
    latest_id = query if query.scalar() else 0

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
    notices = get_notices()
    get_updated_notices(notices)
