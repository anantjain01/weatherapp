# from .views import *    
# also used for import all views file in this for use this we write function name       {i.e index} in place of {i.e views.index}


from django import views
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='home')
]