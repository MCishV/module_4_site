from django.urls import path
from .views import index, topsellers, register, advp, adv, login, profile

urlpatterns = [
    path('', index),
    path('top-sellers', topsellers),
    path('register', register),
    path('advertisement-post', advp),
    path('advertisement', adv),
    path('login', login),
    path('profile', profile),
]
