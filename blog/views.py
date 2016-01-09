from django.shortcuts import render
from django.http import Http404
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', context)

def detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exit")
    return render(request, 'blog/detail.html', {'blog': blog})