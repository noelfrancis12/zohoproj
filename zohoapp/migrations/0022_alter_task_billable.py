# Generated by Django 4.2 on 2023-06-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0021_alter_task_billable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='billable',
            field=models.CharField(blank=True, default='Not Billed', max_length=255, null=True),
        ),
    ]