from django.conf import settings
from django.db import models


class Post(models.Model):
    auther = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    # upload_to 하위폴더만들어 저장하는 옵션
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"Custom object ({self.id})"
        return self.message
    # 모델 변수에 없는 별도의 변수를 models.py에서 만들때의 예, admin.py에서 만들수 도 있음.
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    # post_id 필드가 자동생성된다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # Post로 사용해도 되고 'Post'로 사용해도 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)
    # Post 클래스에 필드를 만들어서 사용해도 된다.

    def __str__(self):
        return self.name
