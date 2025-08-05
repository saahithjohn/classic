from django.urls import path

urlpatterns = [
    # ...existing code...
]
from django.urls import path
from . import views

app_name = 'electricity'

urlpatterns = [
    path('', views.usage_list, name='usage_list'),
    path('create/', views.usage_create, name='usage_create'),
    path('<int:pk>/', views.usage_detail, name='usage_detail'),
    path('<int:pk>/edit/', views.usage_update, name='usage_update'),
    path('<int:pk>/delete/', views.usage_delete, name='usage_delete'),
]
