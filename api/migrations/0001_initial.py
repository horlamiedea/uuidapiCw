# Generated by Django 3.1 on 2022-01-16 00:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
