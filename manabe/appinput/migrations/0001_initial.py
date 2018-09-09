# Generated by Django 2.1 on 2018-08-11 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='描述')),
                ('change_date', models.DateTimeField(auto_now=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('jenkins_job', models.CharField(max_length=255, verbose_name='JENKINS JOB名称')),
                ('is_restart_status', models.BooleanField(default=True, verbose_name='是否重启')),
                ('app_args', models.CharField(blank=True, max_length=128, null=True, verbose_name='APP脚本参数')),
                ('op_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='op_user', to=settings.AUTH_USER_MODEL, verbose_name='操作用户')),
            ],
            options={
                'db_table': 'App',
                'ordering': ('-add_date',),
            },
        ),
    ]
