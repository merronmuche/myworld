
from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('', views.index),
    path('ccc/',views.new_mod)
]
