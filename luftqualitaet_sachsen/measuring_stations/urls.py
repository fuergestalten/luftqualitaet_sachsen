# -*- coding: utf-8 -*-
from django.conf.urls import url

from measuring_stations import views


urlpatterns = [
    url(r'^$', views.overview, name='measuring_stations_measuringpoint_overview'),
    url(r'^station/(?P<slug>[-\w]+)/$', views.MeasuringPointDetailView.as_view(),
        name='measuring_stations_measuringpoint_detail'),
    url(r'^station/(?P<slug>[-\w]+)\.csv$', views.MeasuringPointCSVView.as_view(),
        name='measuring_stations_measuringpoint_csv'),
]
