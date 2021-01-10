from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name='dashboard'),
    path('items/', views.itemsView, name='items'),
    path('edit/', views.edit, name='edit'),
]
