from django.urls import path
from . import views

app_name = 'power_estimation'

urlpatterns = [
    path('', views.index, name='index'),
    path('open/', views.openfile, name='openfile'),
    # path('', views.indexview, name='index'),
    path('charts/', views.chartsview, name='charts'),
    path('tables/', views.tablesview, name='tables'),
]