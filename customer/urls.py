from django.urls import path
from .views import *

urlpatterns= [
    path('offer/', ListCreateOffer.as_view()),
    
]