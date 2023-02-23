from django.urls import path

from . import  views #From All import Views

#For mappinglist of mappings
urlpatterns = [
    path('', views.home, name = 'home')#user reuests, function name, name

]

