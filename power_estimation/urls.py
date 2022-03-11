from django.urls import path
from . import views

app_name = 'power_estimation'

urlpatterns = [
    path('', views.index, name='index'),
    path('test2/', views.test2, name='test2'),
    path('charts/', views.chartsview, name='charts'),
    path('tables/', views.tablesview, name='tables'),
    path('user/', views.userview, name='user'),
    path('user2/', views.userview2, name='user2'),
    path('expert/', views.expertview, name='expert'),
    path('select/', views.selected, name='selected'),
    path('filepath/', views.filepath, name='filepath'),
    path('filepath2/', views.filepath2, name='filepath2'),
    #path('mychart/', views.chartview, name='mychart'),
]