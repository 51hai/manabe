# Generated by Django 2.1 on 2018-08-20 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinput', '0002_auto_20180818_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='op_log_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
