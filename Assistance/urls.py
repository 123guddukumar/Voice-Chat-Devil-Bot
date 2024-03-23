from django.urls import path,include
from Assistance import views

urlpatterns = [
    path("",views.chatbot,name='chatbot'),
    path("home/",views.index,name='home'),
    path("home/register/",views.register,name='register'),
    path("home/loginUser/",views.loginUser,name='loginUser'),
    path("home/about/",views.about,name='about'),
]
