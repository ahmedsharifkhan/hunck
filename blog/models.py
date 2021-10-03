from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model



class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    # slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    author=models.CharField(max_length=20)
    author_pic = models.ImageField()
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    

    def __str__(self):
        return self.title + " by " + self.author