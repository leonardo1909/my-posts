# Generated by Django 3.0.1 on 2020-01-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20191228_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(db_column='ds_titulo', max_length=100, unique=True),
        ),
    ]
