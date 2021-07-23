from django.urls import path, include
from . import views


urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
    path('social/', views.social),
]
