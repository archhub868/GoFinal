
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('doctors/', views.doctors, name='doctors'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('contact/', views.contact, name='contact'),
    path('myrecords/', views.myrecords, name='myrecords'),
    path('delete_contact/<int:id>', views.delete_contact),


]
