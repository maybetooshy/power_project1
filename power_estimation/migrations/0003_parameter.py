# Generated by Django 4.0.2 on 2022-02-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power_estimation', '0002_rename_img_test_table_area_remove_test_table_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icc1', models.FloatField(max_length=10)),
                ('icc2', models.FloatField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('sample', models.CharField(max_length=10)),
                ('Field5', models.FloatField(max_length=10)),
            ],
        ),
    ]
