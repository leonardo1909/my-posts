from django.contrib import admin

from post.models import Post, Categoria, Tag
from post.models import PostCategoria, PostTag

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(PostCategoria)
admin.site.register(PostTag)
