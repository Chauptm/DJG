from django.urls import path
from quickstart import views

app_name='quickstart'
urlpatterns = [
    path("",views.quick.as_view(), name="quick"),
]