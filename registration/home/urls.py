from django.contrib import admin
from django.urls import path,include
from .views import CustomPasswordResetView,index,dashboard,SignUpView

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]

from django.urls import path


