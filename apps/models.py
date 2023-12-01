from tortoise import Tortoise
from tortoise import Tortoise, fields
from tortoise.models import Model


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
    try:
        await Tortoise.generate_schemas()
    except:
        print("Schemas already exist!")


class Admin(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=256)
    tg_id = fields.IntField(pk=True)


class Psychologist(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=256)
    tg_id = fields.IntField(pk=True)
    is_free = fields.BooleanField(default=True)

    schedules: fields.ReverseRelation["Schedule"]


class Schedule(Model):
    id = fields.IntField(pk=True)
    psychologist = fields.ForeignKeyField("models.Psychologist", to_field='id', related_name="schedules")
    start_time = fields.CharField(max_length=256)
    end_time = fields.CharField(max_length=256)
    day_of_week = fields.CharField(max_length=256)
