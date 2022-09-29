# Generated by Django 4.1 on 2022-09-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_cuenta', models.IntegerField(blank=True, null=True)),
                ('monto', models.IntegerField(blank=True, null=True)),
                ('tipo_operacion', models.TextField(blank=True, null=True)),
                ('hora', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
    ]