# Generated by Django 4.0.2 on 2022-02-28 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('power_estimation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_table',
            old_name='img',
            new_name='area',
        ),
        migrations.RemoveField(
            model_name='test_table',
            name='status',
        ),
        migrations.AddField(
            model_name='test_table',
            name='introduction',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_table',
            name='party_number',
            field=models.IntegerField(default=0),
        ),
    ]
