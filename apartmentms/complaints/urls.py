from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('create/', views.complaint_create, name='complaint_create'),
    path('<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('<int:pk>/edit/', views.complaint_update, name='complaint_update'),
    path('<int:pk>/delete/', views.complaint_delete, name='complaint_delete'),
]
