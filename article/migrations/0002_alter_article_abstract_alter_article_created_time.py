# Generated by Django 4.0 on 2022-01-02 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
