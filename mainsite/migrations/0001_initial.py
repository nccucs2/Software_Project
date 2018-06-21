# Generated by Django 2.0.5 on 2018-06-21 18:23

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
                ('Semester', models.IntegerField(null=True)),
                ('course_name', models.TextField()),
                ('credit', models.CharField(blank=True, max_length=5)),
                ('teacher', models.TextField()),
                ('course_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('course_category', models.CharField(blank=True, max_length=5)),
                ('deparment', models.TextField(blank=True)),
                ('course_type', models.CharField(blank=True, max_length=5)),
                ('general_type', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='course_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.SmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.course')),
            ],
        ),
        migrations.CreateModel(
            name='gpa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa_count', models.FloatField()),
                ('grade_range', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='personal_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('id_number', models.CharField(max_length=10)),
                ('guardian', models.CharField(max_length=10)),
                ('birth', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('english_name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
        migrations.AddField(
            model_name='course_grade',
            name='grade_range',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainsite.gpa'),
        ),
        migrations.AddField(
            model_name='course_grade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
