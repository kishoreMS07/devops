# Generated by Django 3.2.7 on 2021-11-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.ImageField(upload_to='')),
            ],
        ),
    ]
