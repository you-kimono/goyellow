from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EnterpriseListView.as_view(), name="index"),
    url(r'^(?P<pk>\d+)/$', views.EnterpriseDetailsView.as_view(), name="details"),
    url(r'^new/$', views.new_enterprise, name="new"),
]
