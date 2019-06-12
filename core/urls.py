from django.urls import path, include
from .views import Produto

urlpatterns = [
   path('view/', Produto, name='Produto'),
]
