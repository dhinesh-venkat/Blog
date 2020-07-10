from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class DetailedView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = "delete.html"