# Generated by Django 4.2.8 on 2023-12-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gatepasses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gatepass",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]