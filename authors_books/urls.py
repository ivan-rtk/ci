from rest_framework.routers import DefaultRouter

from authors_books.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')

urlpatterns = router.urls
