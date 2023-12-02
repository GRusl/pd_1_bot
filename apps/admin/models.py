from tortoise import fields
from tortoise.models import Model


class Schedule(Model):
    pk = fields.IntField(pk=True)
    psychologist = fields.ForeignKeyField('psychologist.Psychologist')
    start_time = fields.CharField(max_length=256)
    end_time = fields.CharField(max_length=256)
    day_of_week = fields.CharField(max_length=256)


class Admin(Model):
    pk = fields.IntField(pk=True)
    username = fields.CharField(max_length=256)
    tg_id = fields.IntField()
