# Generated by Django 3.2.9 on 2022-02-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20220206_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='support',
            field=models.IntegerField(),
        ),
    ]
