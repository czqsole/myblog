from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', context)