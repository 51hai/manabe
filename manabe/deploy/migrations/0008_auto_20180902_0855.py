# Generated by Django 2.1 on 2018-09-02 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0007_history_deploy_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='type',
            new_name='do_type',
        ),
    ]
