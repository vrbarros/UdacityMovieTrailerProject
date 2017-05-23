from django.conf.urls import url
from MovieTrailerApp import views

urlpatterns = [
    url(r'^$', views.vwIndex.as_view()),
]
