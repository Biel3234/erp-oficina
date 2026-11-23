from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from stock.services import register_movement


def _user_or_none(user):
    return user if user is not None and user.is_authenticated else None


def take_items_from_stock(items, user):
    """Dá baixa no estoque (OUT) das peças colocadas na OS."""
    for item in items:
        try:
            register_movement(
                movement_type='OUT',
                part_id=item.part_id,
                quantity=item.quantity,
                created_by=_user_or_none(user),
            )
        except DjangoValidationError:
            raise ValidationError({
                'items': f'Estoque insuficiente para a peça "{item.part}" '
                         f'(pedido: {item.quantity}).'
            })


def return_items_to_stock(items, user):
    """Devolve ao estoque (IN) as peças retiradas da OS."""
    for item in items:
        register_movement(
            movement_type='IN',
            part_id=item.part_id,
            quantity=item.quantity,
            created_by=_user_or_none(user),
        )
