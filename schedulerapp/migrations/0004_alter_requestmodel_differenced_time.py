# Generated by Django 4.0.4 on 2022-06-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulerapp', '0003_remove_requestmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmodel',
            name='differenced_time',
            field=models.CharField(max_length=300, null=True),
        ),
    ]