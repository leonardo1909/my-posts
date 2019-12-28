from django.db import models
from uuid import uuid4


class Post(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column='cd_post'
    )
    titulo = models.CharField(
        max_length=100,
        db_column='ds_titulo'
    )
    descricao = models.CharField(
        max_length=300,
        db_column='ds_descricao'
    )
    conteudo = models.CharField(
        max_length=1000,
        db_column='ds_conteudo'
    )
    data_publicacao = models.DateTimeField(
        db_column='dt_publicacao',
        auto_now=True
    )

    class Meta:
        db_table = 'tb_post'

    def __str__(self):
        return f'{self.codigo}'
