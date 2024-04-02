from django.urls import path
from .views import *

urlpatterns = [
    path('home/<int:pk>', home, name='home1'),
    path('integer/<int:pk>', home, name='home'), #
    path('string/<str:pk>', string, name='home'), 
    path('slugs/<slug:pk>', home, name='home'),
    path('paths/<path:pk>', home, name='home'),
    path('combination/<path:pk>/<slug:abcst>/<str:abc>/<int:st>',combination , name='home1'),
]
