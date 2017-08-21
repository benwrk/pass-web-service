from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from service_app import views

urlpatterns = [
    url(r'^floors/$', views.FloorList.as_view(), name='floor-list'),
    url(r'^floors/(?P<pk>[0-9]+)/$', views.FloorDetail.as_view(), name='floor-detail'),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='group-detail'),
    url(r'^wards/$', views.WardList.as_view(), name='ward-list'),
    url(r'^wards/(?P<pk>[0-9]+)/$', views.WardDetail.as_view(), name='ward-detail'),
    url(r'^boxes/$', views.BoxList.as_view(), name='box-list'),
    url(r'^boxes/(?P<pk>[0-9]+)/$', views.BoxDetail.as_view(), name='box-detail'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
