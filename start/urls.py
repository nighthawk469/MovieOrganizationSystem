from django.conf.urls import *

from start import views
#from blog.views import BlogPostList

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),

]