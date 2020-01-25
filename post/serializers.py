from rest_framework import serializers

from post.models import (Post, Tag, Categoria, PostCategoria, PostTag)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'nome', 'descricao',
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'nome'
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(
        required=False,
        many=True
    )
    tags = TagSerializer(
        required=False,
        many=True
    )

    class Meta:
        model = Post
        fields = [
            'titulo', 'descricao',
            'conteudo', 'categorias', 'tags'
        ]

    def create(self, validated_data):
        possui_tag = validated_data.pop('tags', None)
        possui_categoria = validated_data.pop('categorias', None)

        post = Post.objects.create(**validated_data)

        tags_objects = []
        tag_post = []
        if possui_tag:
            tags = Tag.objects.all()
            tags_nomes = tags.values_list('nome', flat=True)
            for tag in possui_tag:
                if tag['nome'] not in tags_nomes:
                    tag_instance = Tag(
                        nome=tag['nome']
                    )
                    tags_objects.append(tag_instance)
                else:
                    tag_instance = tags.filter(
                        nome=tag['nome']
                    ).first()

                tag_post.append(
                    PostTag(
                        tag=tag_instance,
                        post=post
                    )
                )
            if tags_objects:
                Tag.objects.bulk_create(tags_objects)

            PostTag.objects.bulk_create(tag_post)

        return post
