from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/create$', views.create_blog, name='create_blog'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
]