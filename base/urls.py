from django.urls import path, include
from base import views

urlpatterns = [

    path('', views.get_personality, name='home'),

]
