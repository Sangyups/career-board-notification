import requests
from bs4 import BeautifulSoup

from const import URL, URL_QUERY
from logger import logger


def get_text_from_element(element):
    return element.get_text().strip()


def get_notices_from_career_board():
    notice_list = []
    try:
        response = requests.get(URL + URL_QUERY)
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
        logger.info(f"데이터 수집이 완료되었습니다.")
    except Exception as e:
        logger.error(f"{e}")

    return notice_list
