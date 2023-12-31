# Generated by Django 4.2 on 2023-07-01 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0023_alter_project1_billing_alter_project1_budget_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernamezz', models.CharField(blank=True, max_length=255, null=True)),
                ('emailzz', models.CharField(blank=True, max_length=255, null=True)),
                ('projnn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.project1')),
                ('userss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
