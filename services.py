from models import Notice


def save_notices(updated_notices):
    Notice.insert_many(updated_notices).execute()
