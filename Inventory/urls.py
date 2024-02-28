from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomePage),
    path('about/',aboutpage),
    path('contact/',contactpage),
    path('services/',servicespage),
    path('products/add/',productsadd),
    path("products/",AllProducts)
]