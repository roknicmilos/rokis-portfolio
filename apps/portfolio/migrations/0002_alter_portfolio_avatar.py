# Generated by Django 5.1.1 on 2024-09-21 12:53

import apps.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="avatar",
            field=models.ImageField(
                null=True,
                upload_to="portfolio/images/",
                validators=[apps.common.validators.MaxFileSizeValidator(100)],
                verbose_name="avatar",
            ),
        ),
    ]
