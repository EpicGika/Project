from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


class PostList(ListView):
    model = Post
    # template_name = "post_list.html"
