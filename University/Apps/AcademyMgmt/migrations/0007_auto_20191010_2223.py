# Generated by Django 2.2.6 on 2019-10-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademyMgmt', '0006_auto_20191010_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='SecLastName',
        ),
        migrations.AlterField(
            model_name='student',
            name='LastName',
            field=models.CharField(max_length=35),
        ),
    ]
