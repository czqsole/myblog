from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/create$', views.create_blog, name='create_blog'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^boot_test', views.show_boot_test, name='show_boot_test'),
    url(r'mark', views.show_mark, name='show_mark'),
]