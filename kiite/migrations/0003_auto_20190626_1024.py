# Generated by Django 2.1 on 2019-06-26 01:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiite', '0002_story_ps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.TextField(max_length=250, validators=[django.core.validators.MinLengthValidator(60)], verbose_name='KIITE'),
        ),
    ]
