from django.urls import path
from recipes.views import bargain_chef_flow, index

urlpatterns = [
    path('', index),
    path('bargainChefFlow', bargain_chef_flow),
]