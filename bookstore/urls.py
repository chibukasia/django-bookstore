from django.urls import path, include
from .views import BookList, BookDetails, AuthorList, AuthorDetails


urlpatterns = [
    path('books/', BookList.as_view(), name='books' ),
    path('books/<int:pk>/', BookDetails.as_view(), name='book-details'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetails.as_view(), name='author-details'),
]