# Generated by Django 4.2.10 on 2024-02-17 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='vote',
        ),
    ]
