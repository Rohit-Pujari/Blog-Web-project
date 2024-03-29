# Generated by Django 5.0.1 on 2024-01-11 14:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name=models.AutoField(
                    primary_key=True, verbose_name="timestamp"
                ),
            ),
        ),
    ]
