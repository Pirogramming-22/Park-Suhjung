from django.db import models
from django.contrib.auth.models import User
from devtools.models import DevTool 
from PIL import Image  # Pillow 라이브러리의 Image 모듈 임포트
import os
from django.conf import settings

#class Idea(models.Model):
   # title = models.CharField(max_length=200)
   # thumbnail = models.ImageField(upload_to='ideas/thumbnails/')
    #interest = models.IntegerField(default=0)
   # created_at = models.DateTimeField(auto_now_add=True)
   # updated_at = models.DateTimeField(auto_now=True)

   # def __str__(self):
       # return self.title


class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ideas/',null=True)
    thumbnail = models.ImageField(upload_to='ideas/thumbnails/', blank=True, null=True)
    content = models.TextField(default="입력하세요")
    interest = models.PositiveIntegerField(default=0)
    
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name='ideas',default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #wishlist = models.BooleanField(default=False)  # 찜 여부 추가
    #wishlist = models.ManyToManyField(User, related_name='starred_ideas', blank=True)  # 추가
        
    
    @property
    def likes(self):
        """찜한 개수를 반환"""
        return self.stars.count()
    def save(self, *args, **kwargs):
        # 기존 저장 로직
        super().save(*args, **kwargs)

        # 썸네일 생성
        if self.image and not self.thumbnail:
            self.create_thumbnail()

    def create_thumbnail(self):
        """이미지 필드를 기반으로 썸네일 생성"""
        img = Image.open(self.image)
        img.thumbnail((300, 300))  # 썸네일 크기 설정
        # 썸네일 경로 생성
        thumbnail_dir = os.path.join(settings.MEDIA_ROOT, 'ideas/thumbnails')
        os.makedirs(thumbnail_dir, exist_ok=True)  # 디렉토리 생성

        thumbnail_path = os.path.join(thumbnail_dir, os.path.basename(self.image.name))
        
        # 썸네일 파일 저장
        img.save(thumbnail_path)
        # 썸네일 필드에 경로 저장
        self.thumbnail = thumbnail_path
        self.save(update_fields=['thumbnail'])


class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_starred = models.BooleanField(default=False)  # 찜 상태

    class Meta:
        unique_together = ('idea', 'user')  # 유저가 하나의 아이디어에만 한 번 찜 가능
