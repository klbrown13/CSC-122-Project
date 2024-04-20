from django.urls import path

from .views import (
    PostListView,
    PostDetailView, # new
    PostUpdateView, # new
    PostDeleteView, # new
    PostCreateView, # new
)

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), 
         name="post_detail"), # new
    path("<int:pk>/edit/", PostUpdateView.as_view(), 
         name="post_edit"), # new
    path("<int:pk>/delete/", PostDeleteView.as_view(), 
         name="post_delete"), # new
    path("new/", PostCreateView.as_view(), name="post_new"), # new
    path("", PostListView.as_view(), 
         name="post_list"), # new
]