# Generated by Django 2.2.5 on 2019-09-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademyMgmt', '0004_course_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='DOC',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]