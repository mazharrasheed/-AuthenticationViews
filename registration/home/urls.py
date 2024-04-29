from django.contrib import admin
from django.urls import path,include
from .views import CustomPasswordResetView,index,dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),


    
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_change'),
]

