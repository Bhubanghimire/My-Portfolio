# Generated by Django 4.0 on 2021-12-12 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
        ('accounts', '0002_remove_myuser_phone_remove_myuser_verified_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.configchoice')),
            ],
        ),
    ]
