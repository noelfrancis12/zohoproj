# Generated by Django 4.2 on 2023-06-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0018_usernamez'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernamez',
            name='emailz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usernamez',
            name='usernamez',
            field=models.CharField(max_length=255, null=True),
        ),
    ]