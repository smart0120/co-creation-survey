# Generated by Django 3.1.3 on 2020-11-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurship',
            name='classifications_detail',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
