from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from main import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    ### url(r'^throwaway/$', views.ThrowawayView.as_view(), name='throwaway'),
)
