from notification.discord import notify_via_discord
from notification.github_issue import notify_via_github_issue
from notification.slack import notify_via_slack


def notify_notices(notices):
    notify_via_slack(notices)
    notify_via_discord(notices)
    notify_via_github_issue(notices)
