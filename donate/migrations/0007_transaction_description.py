# Generated by Django 3.1.6 on 2021-04-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_auto_20210415_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
