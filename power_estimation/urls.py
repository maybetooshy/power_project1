from django.urls import path
from . import views

app_name = 'power_estimation'

urlpatterns = [
    path('', views.index, name='index'),
    path('test2/', views.test2, name='test2'),
    path('charts/', views.chartsview, name='charts'),
    path('tables/', views.tablesview, name='tables'),
    path('user/', views.userview, name='user'),
    path('expert/', views.expertview, name='expert'),
    path('select/', views.selected, name='selected'),
    #path('mychart/', views.mychart, name='mychart'),
]