from notification.discord import notify_via_discord
from notification.slack import notify_via_slack


def notify_notices(notices):
    notify_via_slack(notices)
    notify_via_discord(notices)
