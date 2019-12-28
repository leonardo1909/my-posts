# Generated by Django 3.0.1 on 2019-12-28 01:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_post', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(db_column='ds_titulo', max_length=100)),
                ('descricao', models.CharField(db_column='ds_descricao', max_length=300)),
                ('conteudo', models.CharField(db_column='ds_conteudo', max_length=1000)),
                ('data_publicacao', models.DateTimeField(db_column='dt_publicacao')),
            ],
            options={
                'db_table': 'tb_post',
            },
        ),
    ]
