# Generated by Django 2.0.5 on 2018-06-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpa',
            name='grade_range',
            field=models.CharField(max_length=10),
        ),
    ]
