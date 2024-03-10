from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts
from datetime import datetime
class PostsList(ListView):
    model = Posts
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context
# Create your views here.

class PostsDetail(DetailView):
    model = Posts
    template_name = 'news.html'
    context_object_name = 'post'
