# Generated by Django 4.2 on 2023-07-04 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0024_usercreate'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='c_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer'),
        ),
    ]