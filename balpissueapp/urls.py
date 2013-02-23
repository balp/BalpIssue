'''
Created on 23 feb 2013

@author: balp
'''
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from balpissueapp.models import Issue

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Issue.objects.order_by('-pub_date')[:5],
            context_object_name='latest_issue_list',
            template_name='balpissueapp/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Issue,
            template_name='balpissueapp/detail.html')),
)