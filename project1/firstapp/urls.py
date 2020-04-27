from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_name_view, name='form')
]
