from django.urls import path, include
from django.shortcuts import render
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:i_slug>/', views.item, name='prod_det'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('cart/', include('cart.urls')),
    path('search', views.searching, name='search'),
    path('base', views.base, name='base'),
]
