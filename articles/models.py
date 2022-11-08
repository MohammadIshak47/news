from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("articles:article_detail", args=[str(self.id)])
    
class Comment(models.Model):
    article = models.ForeignKey(Articles,on_delete = models.CASCADE)
    comment = models.CharField(max_length = 140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'comments',
    )    
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("articles:article_list")
    
    
    
