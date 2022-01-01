def test_demo():
    assert True

# import pytest
# from django.urls import reverse
# from rest_framework import status
#
# from authors_books.models import Book
#
#
# @pytest.mark.django_db
# def test_get_book(api_client, books_factory):
#     """проверка получения книги"""
#     books_factory(_quantity=7)
#     book = Book.objects.first()
#     url = reverse('books-detail', kwargs={'pk': book.id})
#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['name'] == book.name
#
#
# @pytest.mark.django_db
# def test_get_book_list(api_client, books_factory):
#     """проверка получения списка книг"""
#     books_factory(_quantity=5)
#     url = reverse('books-list')
#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) == 5
#
#
# @pytest.mark.django_db
# def test_get_book_filtered_by_id(api_client, books_factory):
#     """проверка фильтрации списка книг по id"""
#     books_factory(_quantity=7)
#     book = Book.objects.first()
#     url = reverse('books-list')
#     response = api_client.get(url, data={'id': book.id})
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) == 1
#     assert response.data[0]['id'] == book.id
#
#
# @pytest.mark.django_db
# def test_get_book_filtered_by_name(api_client, books_factory):
#     """проверка фильтрации списка книг по name"""
#     Book.objects.bulk_create([
#         Book(name='Грокаем алгоритмы'),
#         Book(name='A Byte of Python'),
#         Book(name='C# для чайников')
#     ])
#     book = Book.objects.first()
#     url = reverse('books-list')
#     response = api_client.get(url, data={'name': book.name})
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) == 1
#     assert response.data[0]['name'] == book.name
#
#
# @pytest.mark.django_db
# def test_book_create(api_client):
#     """тест успешного создания книги"""
#     url = reverse('books-list')
#     data = {'name': 'A Byte of Python'}
#     response = api_client.post(url, data=data)
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data['name'] == 'A Byte of Python'
#
#
# @pytest.mark.django_db
# def test_book_update(api_client, books_factory):
#     """тест успешного обновления книги"""
#     books_factory(name='A Byte of Python')
#     book = Book.objects.first()
#     data = {'name': 'Грокаем алгоритмы'}
#     url = reverse('books-detail', kwargs={'pk': book.id})
#     response = api_client.patch(url, data=data)
#     assert response.status_code == status.HTTP_200_OK
#     response_j = response.json()
#     assert response_j['id'] == book.id
#     assert response_j['name'] == 'Грокаем алгоритмы'
#
#
# @pytest.mark.django_db
# def test_book_delete(api_client, books_factory):
#     """тест успешного удаления книги"""
#     Book.objects.bulk_create([
#         Book(name='Грокаем алгоритмы'),
#         Book(name='A Byte of Python'),
#         Book(name='C# для чайников')
#     ])
#     book = Book.objects.get(name='C# для чайников')
#     url = reverse('books-detail', kwargs={'pk': book.id})
#     response = api_client.delete(url)
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#     url = reverse('books-list')
#     response = api_client.get(url)
#     assert len(response.data) == 2
#     response_j = response.json()
#     assert response_j[0]['name'] == 'Грокаем алгоритмы'
#     assert response_j[1]['name'] == 'A Byte of Python'
