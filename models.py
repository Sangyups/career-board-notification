import os

from dotenv import load_dotenv
from peewee import *

from const import DATETIME_FORMAT

load_dotenv()

db = MySQLDatabase(
    os.environ.get("DB_NAME"),
    host=os.environ.get("DB_HOST"),
    port=int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER"),
    passwd=os.environ.get("DB_PASSWORD"),
)


class BaseModel(Model):
    class Meta:
        database = db


class Notice(BaseModel):
    notice_id = IntegerField(primary_key=True)
    title = CharField(max_length=100)
    manager = CharField(max_length=20)
    view_counts = IntegerField()
    registered_at = DateTimeField(formats=DATETIME_FORMAT)
    link = TextField()


db.connect()
db.create_tables([Notice])
