from datetime import datetime
from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.utils import formats


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length = 30)    
    post_author = models.CharField(max_length = 200)
    post_text = models.TextField()
    post_time = models.TimeField(auto_now_add = True)
    post_date = models.DateField(auto_now_add = True)
    post_image = models.ImageField(blank = True, upload_to = "blogs", default = 'tempdefault.jpg')

    def __str__(self):
        time = formats.time_format(self.post_time,"H")
        return "{} - {} : {}".format(self.post_title, self.post_date, time)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs = {'pk' : self.id})

    class Meta:
        ordering = ["-post_date"]

class Comment(models.Model):
    comment_date = models.DateField(auto_now_add=True)
    comment_social = models.TextField()
    post = models.ForeignKey('Post' , on_delete = models.CASCADE)

    def __str__(self):
        return self.comment_social

class Tag(models.Model):
    tag_name = models.CharField(max_length = 30)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.tag_name

#class Comments(models.Model):
#    social_comments = models.TextField()
#add comments and tags