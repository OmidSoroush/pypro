# Generated by Django 3.2.6 on 2021-10-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pytutorial', '0008_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at__minute']},
        ),
    ]
