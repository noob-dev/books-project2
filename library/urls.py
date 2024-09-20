from django.urls import path
from .views import book_list, book_detail, category_list, category_detail, author_list, author_detail

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),

    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),

    path('authors/', author_list, name='author_list'),
    path('authors/<int:pk>/', author_detail, name='author_detail'),
]
