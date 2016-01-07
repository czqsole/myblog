from django.test import TestCase
import django
from blog.models import Blog
from django.utils import timezone

django.setup()
Blog.objects.all()
blog1 = Blog(time = timezone.now(), title = "first test blog", summary = 'blog1', article = "test")
blog1.save()

Blog.objects.all()
