# Generated by Django 3.2.6 on 2021-09-16 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', django_quill.fields.QuillField(null=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pythonposts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
