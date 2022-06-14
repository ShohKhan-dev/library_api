
from .models import User, Library, Book, Rent, Category
from rest_framework import serializers




class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='user.first_name')
    category_title = serializers.ReadOnlyField(source='category.title')
    library_name = serializers.ReadOnlyField(source='library.name')


    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'category', 'category_title', 'library', 'library_name', 'description', 'published_date', 'pages', 'language']


class LibrarySerializer(serializers.ModelSerializer):

    library_books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Library
        fields = ['id', 'name', 'address', 'description', 'library_books']



class CategorySerializer(serializers.ModelSerializer):
    # items = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    items = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'items']

class RentSerializer(serializers.ModelSerializer):

    book_title = serializers.ReadOnlyField(source="book.title")



    class Meta:
        model = Rent
        fields = ['id', 'reader', 'book', 'book_title', 'borrowed_date', 'return_date', 'price']



class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'address', 'about_me', 'books')
        read_only_fields = ('books',)

