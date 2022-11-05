import os

from dotenv import load_dotenv

load_dotenv()

URL = "https://cs.korea.ac.kr/cs/board/course.do"
URL_QUERY = "?mode=list&&articleLimit=20"
DATETIME_FORMAT = "%Y.%m.%d"
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
MASTER_GITHUB_TOKEN = os.environ.get("MASTER_GITHUB_TOKEN")
REPO_NAME = os.environ.get("REPO_NAME")
