from django.urls import path
from .views import hello_world
from .views import hello_world_template

urlpatterns = [
    path('', hello_world),
    path('template', hello_world_template),
]
