# Generated by Django 2.0.5 on 2018-06-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='general_type',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
