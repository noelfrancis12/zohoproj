# Generated by Django 4.2 on 2023-06-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0015_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='userz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='newuser',
        ),
    ]
