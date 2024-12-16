from django.urls import path
from  . import views

urlpatterns=[
    path('registration/',views.registration,name='registration'),
    path('kids/',views.kids,name='kids'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
]