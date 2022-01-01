from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя')

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')
    author = models.ManyToManyField(Author, through='BookAuthor', related_name='author')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             verbose_name='книга',
                             related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор')

    class Meta:
        verbose_name = 'автор книги'
        verbose_name_plural = 'авторы книги'
