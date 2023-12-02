from tortoise import fields
from tortoise.models import Model


class Psychologist(Model):
    pk = fields.IntField(pk=True)
    username = fields.CharField(max_length=256)
    tg_id = fields.IntField()
    is_free = fields.BooleanField(default=True)
