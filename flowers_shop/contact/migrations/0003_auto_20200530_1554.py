# Generated by Django 3.0.6 on 2020-05-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
