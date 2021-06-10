from django.contrib import admin
from .models import Post, Comment, Tag 
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)