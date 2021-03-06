# Generated by Django 3.2.9 on 2022-02-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_about_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='cover',
        ),
        migrations.AddField(
            model_name='about',
            name='profile',
            field=models.ImageField(default='sad', upload_to='profile'),
            preserve_default=False,
        ),
    ]
