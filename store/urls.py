from django.contrib import admin
from django.urls import path

from Ecommerce.Ecommerce.urls import urlpatterns
from .views import home


urlpatterns=[
    path('',home)
]
