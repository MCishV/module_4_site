from django.urls import path
from .views import index, topsellers

urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', topsellers, name="sellers"),
]
