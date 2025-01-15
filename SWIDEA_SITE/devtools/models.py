from django.db import models

class DevTool(models.Model):
    name = models.CharField(max_length=100)  # 개발 도구 이름
    kind = models.CharField(max_length=100, blank=True, null=True)  # 개발 도구 종류
    content = models.TextField()  # 개발 도구 설명

    def __str__(self):
        return self.name
