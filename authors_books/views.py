from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from authors_books.models import Book, Author
from authors_books.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().prefetch_related('author')
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'name', 'author']
    ordering_fields = ['name', 'author']


class Books(ListView):
    model = Book
    template_name = 'books/books_list.html'
    queryset = Book.objects.prefetch_related('author')
