# Generated by Django 2.2.5 on 2019-09-29 05:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AcademyMgmt', '0003_auto_20190929_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='DOC',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
