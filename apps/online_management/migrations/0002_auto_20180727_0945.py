# Generated by Django 2.0.6 on 2018-07-27 09:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='troublerecord',
            name='handle_user',
        ),
        migrations.AddField(
            model_name='troublerecord',
            name='handle_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='处理人'),
        ),
    ]
