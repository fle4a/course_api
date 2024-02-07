from tortoise import fields
from tortoise.models import Model


class Task(Model):
    id = fields.UUIDField(pk=True)
    description = fields.TextField()
    completed = fields.BooleanField(default=False)
    due_date = fields.DateField(null=True)
    user = fields.ForeignKeyField('default.User', related_name='tasks')

    def __str__(self):
        return self.description
