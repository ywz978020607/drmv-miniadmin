from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  #分应用，之前urls.py是include
    path('test/',views.test),
    path('test/sub1/',views.test_sub1),
    
    path('esp32_up/',views.esp32_up),
    path('esp32_down/',views.esp32_down),
]
