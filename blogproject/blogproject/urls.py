"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from blogs.views import (
                PostCreateView, 
                PostDetailView, 
                PostListView, 
                PostUpdateView, 
                PostDeleteView, 
                PythonTagView,
                JSTagView,
            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name = "post_list"),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name = "post_detail"),
    path('create/', PostCreateView.as_view(), name = "post_create"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name = "post_update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name = "delete_post"),
    path('pythontags/', PythonTagView.as_view(), name = "python_tags"),
    path('jstags/', JSTagView.as_view(), name = "js_tags"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)