from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('exit/', views.exitJY, name='exitJY'),
    path('book/', views.select, name='select'),
    path('book/insert/', views.insert, name='insert'),
    path('book/insert/result/', views.execInsert, name='execInsert'),
    path('book/delete/', views.delete, name='delete'),
    path('book/delete/result/', views.execDelete, name='execDelete'),
    path('book/update/', views.update, name='update'),
    path('book/update/result/', views.execUpdate, name='execUpdate'),
]