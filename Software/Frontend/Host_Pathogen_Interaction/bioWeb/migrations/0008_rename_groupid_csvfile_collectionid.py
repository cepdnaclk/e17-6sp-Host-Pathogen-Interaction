# Generated by Django 4.0.2 on 2022-03-01 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bioWeb', '0007_rename_colllectionname_collection_collectionname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csvfile',
            old_name='groupId',
            new_name='collectionId',
        ),
    ]