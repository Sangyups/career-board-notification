from github import Github
from github.Repository import Repository

from const import MASTER_GITHUB_TOKEN, REPO_NAME
from logger import logger
from utils.time_utils import get_current_date


def build_issue_message(notices):
    issue_title = get_current_date() + " 채용 정보"
    issue_content = f"**{len(notices)}개의 새로운 채용 공고**가 있습니다.<br/><br/>"
    for notice in notices:
        title, link = notice[1], notice[5]
        issue_content += f'<a href="{link}">{title}</a><br/>\n'
    return issue_title, issue_content


def get_repo():
    try:
        g = Github(MASTER_GITHUB_TOKEN)
        return g.get_user().get_repo(REPO_NAME)
    except Exception as e:
        logger.error(str(e))


def create_github_issue(repo: Repository, title, content):
    try:
        repo.create_issue(title=title, body=content)
    except Exception as e:
        logger.error(str(e))


def notify_via_github_issue(notices):
    repo = get_repo()
    title, content = build_issue_message(notices)
    create_github_issue(repo, title, content)
