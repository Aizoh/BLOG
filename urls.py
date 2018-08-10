from django.conf.urls import url
from . import views
# (?P<id>\d+)/$ <int:id>/$ (?P<username>\w+)/$'
app_name = 'posts'
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),

]