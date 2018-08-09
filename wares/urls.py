from django.urls import path

from . import views

urlpatterns = [
    path('<int:ware_id>/detail/', views.ware_detail, name='ware_detail'),
    path('', views.index, name='index'),
]
