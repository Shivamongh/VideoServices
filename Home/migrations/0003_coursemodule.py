# Generated by Django 3.2.7 on 2021-09-14 10:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_course_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_module_name', models.CharField(max_length=100)),
                ('course_description', ckeditor.fields.RichTextField()),
                ('video_url', models.URLField(max_length=300)),
                ('can_view', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.course')),
            ],
        ),
    ]
