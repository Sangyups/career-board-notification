import json

import requests

from const import DISCORD_WEBHOOK_URL


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
    print(response.text)
