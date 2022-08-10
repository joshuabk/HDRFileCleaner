from django.urls import path

from. import views

urlpatterns = [
   
    path('', views.Import, name = 'Import'),
    path('Hello/', views.Hello, name = 'Hello'),
   
   
   
]