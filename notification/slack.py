import json

import requests

from const import SLACK_WEBHOOK_URL
from logger import logger


def build_slack_message(lst):
    payload = {
        "text": f"{len(lst)}개의 새로운 채용 정보가 있습니다.",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{len(lst)}개의 새로운 채용 정보가 있습니다.*",
                },
            },
            {
                "type": "divider",
            },
        ],
    }
    for item in lst:
        title, link = item[1], item[5]
        payload["blocks"].append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"{title}\n<{link}|보러가기>"},
            }
        )
    return payload


def notify_via_slack(notices):
    payload = build_slack_message(notices)
    response = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
    if response.status_code == 200:
        logger.info("슬랙에 성공적으로 메시지를 전송하였습니다.")
    else:
        logger.error(f"{response.status_code} {response.text} 에러 발생")
