from django.test import TestCase
import django, os, sys
sys.path.append('../')
from myblog import settings
DJANGO_SETTINGS_MODULE='myblog.settings'
from models import Blog
from django.utils import timezone

django.setup()
Blog.objects.all()
blog1 = Blog(pub_time = timezone.now(), title = "first test blog", summary = 'blog1', article = "test")
blog1.save()

Blog.objects.all()
