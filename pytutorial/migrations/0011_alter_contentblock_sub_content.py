# Generated by Django 3.2.6 on 2021-09-13 15:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pytutorial', '0010_alter_contentblock_sub_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblock',
            name='sub_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
