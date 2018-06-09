# Generated by Django 2.0.5 on 2018-06-07 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('AcademicYear', models.IntegerField()),
                ('Semester', models.IntegerField()),
                ('course_name', models.TextField()),
                ('credit', models.DecimalField(decimal_places=1, max_digits=2)),
                ('teacher', models.TextField()),
                ('course_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='course_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.SmallIntegerField()),
                ('grade_range', models.SmallIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='gpa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa_count', models.FloatField()),
                ('grade_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.course_grade')),
            ],
        ),
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('number', models.CharField(max_length=10)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
