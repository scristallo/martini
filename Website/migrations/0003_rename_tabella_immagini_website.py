# Generated by Django 4.2.11 on 2024-12-20 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_rename_website_tabella_immagini'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tabella_immagini',
            new_name='Website',
        ),
    ]
