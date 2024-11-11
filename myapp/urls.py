
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),


]
