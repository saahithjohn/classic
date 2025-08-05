from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('create/', views.notice_create, name='notice_create'),
    path('<int:pk>/', views.notice_detail, name='notice_detail'),
    path('<int:pk>/edit/', views.notice_update, name='notice_update'),
    path('<int:pk>/delete/', views.notice_delete, name='notice_delete'),
]
