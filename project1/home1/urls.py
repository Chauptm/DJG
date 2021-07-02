from django.db import router
from django.urls import path, include
from home1 import views
from rest_framework.routers import DefaultRouter
from home1.auth import CustomAuthToken

router= DefaultRouter()
router.register(r'User', views.UserViewsets)
router.register(r'Product', views.ProductListDetail)
urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/', CustomAuthToken.as_view())

]