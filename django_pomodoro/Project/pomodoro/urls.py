from django.urls import path
from .import views

urlpatterns = [
    path('base/', views.baseview.as_view(), name='base'),
    path('', views.homeview.as_view(), name='home'),
    path('index/', views.indexview.as_view(), name='index'),
    path('con_index/', views.conindexview.as_view(), name='conindex')
]