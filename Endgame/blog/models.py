from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #img = models.ImageField(null=True,blank=True, upload_to='media/')
    img = ResizedImageField(size=[640,480], upload_to='media/', blank=True, null=True,quality=100)
    
    def __str__(self):
        return self.title
