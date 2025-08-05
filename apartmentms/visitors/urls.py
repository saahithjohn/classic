from django.urls import path

urlpatterns = [
    # ...existing code...
]
from django.urls import path
from . import views

app_name = 'visitors'

urlpatterns = [
    path('', views.visitor_list, name='visitor_list'),
    path('create/', views.visitor_create, name='visitor_create'),
    path('<int:pk>/', views.visitor_detail, name='visitor_detail'),
    path('<int:pk>/edit/', views.visitor_update, name='visitor_update'),
    path('<int:pk>/delete/', views.visitor_delete, name='visitor_delete'),
]
