"""Add fecha_de_salida field to Visita

Generated manually for local development. After pulling this change, run:
    python manage.py migrate
"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visitas', '0004_remove_visita_fecha_de_salida'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='fecha_de_salida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
