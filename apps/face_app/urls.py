from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('face/', views.faceCheck), 
    path('face/detect/', views.detect), 

] 
