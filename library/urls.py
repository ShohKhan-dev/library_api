
from django.urls import URLPattern, path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('libraries', LibraryList)
router.register('books', BookList)
router.register('users', UserList)
router.register('categories', CategoryList)
router.register('rents', RentList)

urlpatterns = [
    path('', include(router.urls))
    # path('books/', BookList.as_view(), name="book-list"),
]