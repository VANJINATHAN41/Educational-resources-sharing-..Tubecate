# Generated by Django 2.1.7 on 2019-02-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tube', '0002_notifications_new_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]