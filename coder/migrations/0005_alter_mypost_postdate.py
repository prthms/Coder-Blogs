# Generated by Django 3.2.5 on 2022-02-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0004_alter_mypost_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='postDate',
            field=models.DateTimeField(max_length=40),
        ),
    ]