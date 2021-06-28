from django.urls import path
from products import views

app_name='products'
urlpatterns = [
    path("", views.products , name="products"),
    path("<int:id>/", views.getproducts , name="getproducts"),
]
