# Generated by Django 3.2.5 on 2022-02-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0008_remove_mypost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='thumbnail',
            field=models.ImageField(default='', null=True, upload_to='blog/thumnail/'),
        ),
    ]