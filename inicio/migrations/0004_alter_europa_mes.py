# Generated by Django 4.2.6 on 2023-10-31 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_alter_europa_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='europa',
            name='mes',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
