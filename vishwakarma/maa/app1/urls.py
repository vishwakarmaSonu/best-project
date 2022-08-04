from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('open',views.open,name="open"),
    path('login',views.login,name="login"),
    path('singup',views.singup,name="singup"),

    path('book',views.book,name="book"),
    path('about',views.about,name="about"),
    path('produc',views.produc,name="produc"),
    path('touch',views.touch,name="touch"),
    path('logout',views.logout,name="logout"),
    path('detail',views.detail,name="detail"),
    path('owner',views.owner,name="owner"),
    # dynamic templates
    path('booking/<int:pk_test>',views.booking,name="booking"),


]