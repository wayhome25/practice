from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^posts/new/$', views.new_post, name='new_post'),
]
