from django.contrib import admin

from authors_books.models import Author, Book, BookAuthor


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline]
