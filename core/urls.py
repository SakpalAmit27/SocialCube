from django.urls import path 
#setting up our urls #
from . import views;
#index is the main url #

urlPatterns = [
    path('',views.index,name=index)
    
]