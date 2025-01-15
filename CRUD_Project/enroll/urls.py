from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'), 
    path('crud_operations/', views.crud_operations, name='crud_operations'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update<int:id>/', views.update, name='update'),
]
