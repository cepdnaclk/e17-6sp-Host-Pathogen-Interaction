# Generated by Django 4.0.2 on 2022-03-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioWeb', '0010_alter_csvfile_csvfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='csvFile',
            field=models.FileField(upload_to='bioWeb/csvFiles'),
        ),
    ]