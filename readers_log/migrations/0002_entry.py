# Generated by Django 5.2 on 2025-05-06 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers_log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers_log.title')),
            ],
        ),
    ]
