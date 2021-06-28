from django.urls import path
from home import views

app_name='home'
urlpatterns = [
    path("register/",views.registerUser.as_view(), name="registerUser"),
    path("login/",views.loginUser.as_view(), name="loginUser"),
    path("logout/",views.logoutUser, name="logoutUser"),
    path("private/",views.privatePage.as_view(), name="privatePage"),
]
