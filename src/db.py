import json

import peewee

config = json.loads(open("config.json").read())["DB"]

db = peewee.PostgresqlDatabase(
    database=config["database"],
    user=config["user"],
    password=config["password"],
    host=config["host"],
    port=config["port"]
)

db.connect()


class Task(peewee.Model):
    completed = peewee.BooleanField()
    data = peewee.TextField()

    @staticmethod
    def get_uncompleted() -> list:
        return [x.data for x in Task.select(Task.data).where(Task.completed == False)]

    class Meta:
        database = db


db.create_tables([Task])
