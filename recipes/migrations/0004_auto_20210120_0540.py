# Generated by Django 2.2.6 on 2021-01-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210120_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='Cat_Name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]