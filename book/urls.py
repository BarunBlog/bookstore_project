from django.urls import path
from .views import AuthorList, AuthorDetail

urlpatterns = [
    path('author/list-author/', AuthorList.as_view(), name='list-author'),
    path('author/detail-author/<int:pk>/', AuthorDetail.as_view(), name='detail-author'),
]