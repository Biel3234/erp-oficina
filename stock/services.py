from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Movement, Part


@transaction.atomic
def register_movement(movement_type, part_id, quantity, created_by):

    part = Part.objects.select_for_update().get(id=part_id)

    if movement_type == 'IN':
        part.quantity_in_stock += quantity

    elif movement_type == 'OUT':
        if quantity > part.quantity_in_stock:
            raise ValidationError('Estoque insuficiente')
        part.quantity_in_stock -= quantity

    part.save(update_fields=['quantity_in_stock'])

    return Movement.objects.create(
        movement_type = movement_type,
        part = part,
        quantity = quantity,
        created_by = created_by
    )