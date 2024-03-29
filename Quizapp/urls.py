from . import views
from  django.urls import path, include

urlpatterns = [
path('home',views.home,name="home"),
path('register/',views.register,name= "register"),
path('login/',views.loginn,name= "login"),
path('logout/',views.logoutt,name="logout"),  
]


