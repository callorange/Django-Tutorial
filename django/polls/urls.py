from django.urls import path, re_path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # re_path(r'^$', views.index, name='index'),
    # re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
