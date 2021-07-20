from django.urls import path, include
from mybook import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'author', views.AuthorViewsets)
router.register(r'book', views.BookViewsets)
router.register(r'store', views.StoreViewsets)
router.register(r'publisher', views.PublisherViewsets)
urlpatterns = [
    path('',include(router.urls)),
    # path('author/', views.author_list.as_view()),
    # path('author/authors_book_count/', views.author_list.as_view()),
    # path('author/<int:pk>/', views.author_detail.as_view()),
    # path('book/', views.book_list.as_view()),
    # path('book/<int:pk>/', views.book_detail.as_view()),
    # path('store/', views.store_list.as_view()),
    # path('store/<int:pk>/', views.store_detail.as_view()),
    # path('publisher/', views.publisher_list.as_view()),
    # path('publisher/<int:pk>/', views.publisher_detail.as_view()),
]
