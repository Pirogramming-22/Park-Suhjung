from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # 이미지 필드
    created_at = models.DateTimeField(auto_now_add=True)  # 게시물 생성 시간
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # 게시물과 연결
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # 작성자
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"  # 댓글 일부 표시