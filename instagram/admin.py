from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo_tag', 'message',
                    'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']  # 링크 구현하기
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    # 클래스에 없는 변수를 Admin에서 만들기:  그러나,  model.py에서 만들어서 사용할 수 도 있음.

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src ="{post.photo.url}" style="width : 72px"/>')
        return None  # photo가 없으면 None을 반환하라.

    # post.photo.url 이미지의 url,
    # post.photo.path 이미지의 절대경로를 알고 싶을때

    def message_length(self, post):  # Post클래스를 post객체로 받는다.
        # 여기서 객체 이름을 tost로 바꾸어서 해도 된다.
        return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
