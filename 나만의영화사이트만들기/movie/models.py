from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()

    published_date = models.DateTimeField(
            blank=True, null=True)

    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    year = models.IntegerField(null=True)    
    genre = models.CharField(
        max_length=50,
        choices= [
        ('액션', '액션'),
        ('드라마', '드라마'),
        ('코믹', '코믹'),
        ('호러', '호러'),
        ('로맨스', '로맨스'),
        ('SF', 'SF'),
        ],  
        default='액션'
    )

    pd = models.CharField(max_length=200,null=True)
    actors = models.CharField(max_length=500,null=True)
    running_time = models.CharField(max_length=200,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title