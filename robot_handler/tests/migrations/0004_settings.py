# Generated by Django 4.1.3 on 2022-12-05 21:17

from django.db import migrations, models
import tests.models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_rename_suite_testcase_test_suite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_location', models.FilePathField(path=tests.models.images_path)),
            ],
        ),
    ]