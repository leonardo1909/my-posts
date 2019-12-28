from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    # titulo = serializers.CharField()
    # descricao = serializers.CharField()
    # conteudo = serializers.CharField()

    class Meta:
        model = Post
        fields = [
            'titulo', 'descricao',
            'conteudo'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

