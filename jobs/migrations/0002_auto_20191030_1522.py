# Generated by Django 2.0.2 on 2019-10-30 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagefun',
        ),
    ]
