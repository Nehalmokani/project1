from django.urls import path
from .views import *

urlpatterns = [
    path('cal/',calc,name='calcu'),
    path('registernew/',registernew),
    path('new/<int:id>',newfun),
    path('p/',pro,name='prod'),
    path('odd/',odd),
    path('table/',table),
    path('student/',student),
    path('master/',master,name='master'),
    path('a/',a),
    path('b/',b),
    path('prime/',prime),
    path('fec/',fec),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('login/',login,name='login'),
    path('r/',r,name='r'),
    path('book/',bookview),
    path('register/',register),
    path('view/<int:pk>',bookviewpr,name='bookviewpr'),
    path('search/', search, name='search'),
    
]
