import json

import requests

from const import DISCORD_WEBHOOK_URL
from logger import logger


def build_discord_message(lst):
    payload = {
        "embeds": [
            {
                "title": "새로운 채용 공고 알림",
                "description": f"{len(lst)}개의 새로운 채용 정보가 있습니다.",
                "fields": [],
                "color": 5814783,
            }
        ]
    }
    for item in lst:
        title, link = item[1], item[5]
        field = {"name": title, "value": f"[보러가기]({link})"}
        payload["embeds"][0]["fields"].append(field)

    return payload


def notify_via_discord(notices):

    url = DISCORD_WEBHOOK_URL
    headers = {
        "Content-Type": "application/json",
    }

    payload = build_discord_message(notices)

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        logger.info("디스코드에 성공적으로 메시지를 전송하였습니다.")
    else:
        logger.error(f"{response.status_code} {response.text} 에러 발생")
