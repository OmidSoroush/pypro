# Generated by Django 3.2.6 on 2021-10-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pytutorial', '0007_auto_20211006_0942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at__hour']},
        ),
    ]