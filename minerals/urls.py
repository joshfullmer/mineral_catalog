from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='mineral_list'),
    url(r'(?P<mineral_id>\d+)/$', views.mineral_detail, name='mineral_detail'),
    url(r'random/', views.random_mineral, name='random_mineral'),
]
