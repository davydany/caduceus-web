from django.conf.urls import url

from monitor_admin.views import (
    ProjectListView, ProjectCreateView, ProjectDeleteView,
    ProjectUpdateView, ProjectDetailView)
from monitor_admin.api.views import RequestViewSet


urlpatterns = [

    # project-specific
    url(r'^$', ProjectListView.as_view(), name='project-list'),
    url(r'^create/$', ProjectCreateView.as_view(), name='project-create'),
    url(r'^delete/(?P<pk>\d+)/$', ProjectDeleteView.as_view(), name='project-delete'),
    url(r'^update/(?P<pk>\d+)/$', ProjectUpdateView.as_view(), name='project-update'),
    url(r'^detail/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='project-detail'),

    # request specific
    url(r'^api/project/(?P<project_id>[\w\d\-]{36})/request/$',
        RequestViewSet.as_view(), name='request-api'),
]
