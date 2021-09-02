# Generated by Django 3.2.6 on 2021-09-02 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pytutorial', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PythonPost',
            new_name='Post',
        ),
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pytutorial.post')),
            ],
        ),
    ]
