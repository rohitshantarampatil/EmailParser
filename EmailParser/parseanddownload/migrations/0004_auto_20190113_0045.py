# Generated by Django 2.1.3 on 2019-01-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parseanddownload', '0003_auto_20190112_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talksdata',
            old_name='Date',
            new_name='DateofWorkshop',
        ),
        migrations.AddField(
            model_name='talksdata',
            name='DateofEmail',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
