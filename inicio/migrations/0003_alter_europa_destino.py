# Generated by Django 4.2.6 on 2023-10-31 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_africa_america_asia_oceania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='europa',
            name='destino',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
