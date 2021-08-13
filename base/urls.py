from django.urls import path, include
from base import views

urlpatterns = [

    path('', views.get_personality, name='get_personality'),
    path('about_us', views.about_us_view, name='about_us_view'),
    path('contact_us', views.contact_us_view, name='contact_us_view'),
]
