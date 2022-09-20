from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class PostListView(ListView):
    template_name = "posts/lists.html"

class PostDetailView(DetailView):
    template_name = "posts/detail.html"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]