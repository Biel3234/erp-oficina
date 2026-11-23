import django.db.models.deletion
from django.db import migrations, models


def copy_parts(apps, schema_editor):
    WorkOrderParts = apps.get_model('work_orders', 'WorkOrderParts')
    PartWorkOrder = apps.get_model('work_orders', 'PartWorkOrder')
    items = []
    for wop in WorkOrderParts.objects.prefetch_related('part'):
        for part in wop.part.all():
            items.append(PartWorkOrder(
                work_order_parts=wop, part=part, quantity=1, unit_price=part.price,
            ))
    PartWorkOrder.objects.bulk_create(items)


def restore_parts(apps, schema_editor):
    WorkOrderParts = apps.get_model('work_orders', 'WorkOrderParts')
    PartWorkOrder = apps.get_model('work_orders', 'PartWorkOrder')
    for item in PartWorkOrder.objects.all():
        WorkOrderParts.objects.get(pk=item.work_order_parts_id).part.add(item.part_id)


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_movement_created_by'),
        ('work_orders', '0004_remove_workorderparts_parts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartWorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.part')),
                ('work_order_parts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='work_orders.workorderparts')),
            ],
        ),
        migrations.AddConstraint(
            model_name='partworkorder',
            constraint=models.UniqueConstraint(fields=('work_order_parts', 'part'), name='unique_part_per_work_order'),
        ),
        migrations.RunPython(copy_parts, restore_parts),
        migrations.RemoveField(model_name='workorderparts', name='part'),
        migrations.AddField(
            model_name='workorderparts',
            name='part',
            field=models.ManyToManyField(related_name='work_order_parts', through='work_orders.PartWorkOrder', to='stock.part'),
        ),
    ]
