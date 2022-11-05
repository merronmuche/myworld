
from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ccc/',views.new_mod),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
]
