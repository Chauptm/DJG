
from django.db import router
from django.urls import path, include
from home1 import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'User', views.UserViewsets, basename='user')
router.register(r'Product', views.ProductListDetail, basename='product')
urlpatterns = [
    path('',include(router.urls)),
    path('login/', views.Auth.as_view(), name='login'),
    # path('product/', views.ProductList.as_view(), name= 'product_list'),
    # path('product/<int:pk>/', views.ProductDetail.as_view(), name='proudct_detail'),
    # path('user/', views.UserList.as_view(), name= 'user_list'),
    # path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    # path('register/', views.Register.as_view()),
]