from django.urls import path

urlpatterns = [
    # ...existing code...
]
from django.urls import path
from . import views

app_name = 'infrastructure'

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('create/', views.contract_create, name='contract_create'),
    path('<int:pk>/', views.contract_detail, name='contract_detail'),
    path('<int:pk>/edit/', views.contract_update, name='contract_update'),
    path('<int:pk>/delete/', views.contract_delete, name='contract_delete'),
]
