from django.urls import path
from .views import AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    path('author/list-author/', AuthorList.as_view(), name='list-author'),
    path('author/detail-author/<int:pk>/', AuthorDetail.as_view(), name='detail-author'),

    path('book/list-book/', BookList.as_view(), name='list-book'),
    path('book/detail-book/<int:pk>/', BookDetail.as_view(), name='detail-book'),
]