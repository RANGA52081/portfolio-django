# myportfolio/urls.py
from django.contrib import admin
from django.urls import path
from portfolio.views import home # Replace 'yourapp' with your actual app name

urlpatterns = [
    path('', home, name='home'),  # 👈 This handles the empty path
]
