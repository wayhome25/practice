from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new/$', views.new_post, name='new_post'),
	url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
]
