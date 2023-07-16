from enum import Enum

from tortoise import (
    fields,
    models,
)


class CargoTypes(str, Enum):
    """Cargo type enum."""
    glass = 'Glass'
    other = 'Other'


class Rate(models.Model):
    """Rate model."""
    id = fields.IntField(pk=True)
    cargo_type: CargoTypes = fields.CharEnumField(
        CargoTypes, max_length=5, default=CargoTypes.other
    )
    rate = fields.DecimalField(max_digits=4, decimal_places=3)
    date = fields.DateField()
