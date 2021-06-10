from django.db import models
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["post_title","post_author","post_text","post_image"]
    success_url = "/"

class PostUpdateView(UpdateView):
    model = Post
    fields = ["post_title", "post_author", "post_text"]
    template_name_suffix = '_update_form'

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/" 

class PythonTagView(ListView):
    model = Post
    template_name = "blogs/tagspython.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PythonTagView, self).get_context_data(*args, **kwargs)
        #print("this is context", context, "the end of context")
        queryset = Post.objects.filter(tag__tag_name = "Python")
    #print(queryset)
        hello = "this is my message"
        context ["test_list"] = queryset
        context ["word"] = hello
        return context

class JSTagView(ListView):
    model = Post
    template_name = "blogs/tagsjs.html"

    def get_context_data(self, *args, **kwargs):
        context = super(JSTagView, self).get_context_data(*args, **kwargs)
        queryset = Post.objects.filter(tag__tag_name = "JS") # = (name of model__field_name = "") 
        context ["this_list"] = queryset
        return context
