# Generated by Django 3.2.7 on 2021-09-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('Course_description', models.TextField()),
                ('Is_premium', models.BooleanField(default=True)),
                ('Course_image', models.ImageField(upload_to='course.png')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
