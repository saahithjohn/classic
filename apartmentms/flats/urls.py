from django.urls import path
from . import views

urlpatterns = [
    path('', views.flat_list, name='flat_list'),
    path('<int:pk>/', views.flat_detail, name='flat_detail'),
    path('create/', views.flat_create, name='flat_create'),
    path('<int:pk>/edit/', views.flat_update, name='flat_update'),
    path('<int:pk>/delete/', views.flat_delete, name='flat_delete'),
]
