from django.conf.urls import url
from . import views


app_name = 'Comment'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^comment$', views.CommentView, name='comment')
]
