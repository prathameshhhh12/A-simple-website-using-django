from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('index/',views.index, name="home"),
    # path('login',views.loginUser, name="login"),
    # path('logout/',views.logoutUser, name="logout"),
    path("about/" , views.about , name='about'),
    path("services/" , views.services , name='services'),
    path("contact/" , views.contact , name='contact'),
    # path('signup/', views.signup, name='signup'),

     path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),

]
