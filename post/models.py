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
        unique=True,
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
        return f'{self.titulo}'


class Categoria(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column='cd_categoria'
    )

    nome = models.CharField(
        max_length=100,
        unique=True,
        db_column='nm_categoria'
    )

    descricao = models.CharField(
        max_length=300,
        null=True,
        db_column='ds_categoria'
    )

    posts = models.ManyToManyField(
        Post,
        through='PostCategoria',
    )

    class Meta:
        db_table = 'tb_categoria'

    def __str__(self):
        return f'{self.nome}'


class Tag(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column='cd_categoria'
    )

    nome = models.CharField(
        max_length=100,
        db_column='ds_tag'
    )

    posts = models.ManyToManyField(
        Post,
        through='PostTag'
    )

    class Meta:
        db_table = 'tb_tag'

    def __str__(self):
        return f'{self.nome}'


class PostCategoria(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column='cd_post_categoria'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        db_column='fk_post'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        db_column='fk_categoria'
    )

    class Meta:
        db_table = 'tb_post_categoria'

    def __str__(self):
        return f'{self.codigo}'


class PostTag(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column='cd_post_tag'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        db_column='fk_post'
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.DO_NOTHING,
        db_column='fk_tag'
    )

    class Meta:
        db_table = 'tb_post_tag'

    def __str__(self):
        return f'{self.codigo}'
