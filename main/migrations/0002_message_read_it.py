# Generated by Django 3.1.7 on 2021-04-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read_it',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]