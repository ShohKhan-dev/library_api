
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, generics

from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser

class BookList(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'category', 'author']
    search_fields = ['=title', 'description']
    ordering_fields = ['title', 'id']
    ordering = ['id']

    # def get(self, request, format=None):
    #     query = Book.objects.all()
    #     serializer = BookSerializer(query, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryList(viewsets.ModelViewSet):

    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['=name', 'description']
    ordering_fields = ['name', 'id']
    ordering = ['id']


class UserList(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    # permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'username']
    search_fields = ['=username', 'first_name', 'last_name']
    ordering_fields = ['username', 'id']
    ordering = ['id']



class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RentList(viewsets.ModelViewSet):

    queryset = Rent.objects.all()
    serializer_class = RentSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'book', 'reader']
    ordering_fields = ['id']
    ordering = ['id']


