from tortoise import (
    Model,
    fields,
)


class Rate(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=5)
    rate = fields.DecimalField(max_digits=4, decimal_places=3)
