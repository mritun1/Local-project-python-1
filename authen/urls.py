from django.urls import path

from authen import views


urlpatterns = [
    path('',views.authen,name="authen"),
    path('register/',views.register,name="register"),
    
]