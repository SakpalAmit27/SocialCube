from django.urls import path
#setting up our urls #
from . import views
#index is the main url #

urlpatterns = [
    path('',views.index,name='index')
    
]