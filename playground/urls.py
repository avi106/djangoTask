from django.urls import path
from . import views

#URLConf
urlpatterns = [
    # path('home/', views.home, name='home')
    path('hello/', views.say_hello, name='hello')
    
]