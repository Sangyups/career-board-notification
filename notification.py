import json

import requests

from const import SLACK_WEBHOOK_URL


def notify_via_slack(notices):
    payload = {
        "text": f"{len(notices)}개의 새로운 채용 정보가 있습니다.",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{len(notices)}개의 새로운 채용 정보가 있습니다.*",
                },
            },
            {
                "type": "divider",
            },
        ],
    }
    for notice in notices:
        title, link = notice[1], notice[5]
        payload["blocks"].append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"{title}\n<{link}|보러가기>"},
            }
        )
    response = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
