from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.detail, name='detail'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
]