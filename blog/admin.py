from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    ''

admin.site.register(Blog)