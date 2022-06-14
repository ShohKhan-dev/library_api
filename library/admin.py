from django.contrib import admin

from .models import User, Rent, Book, Library, Category
# Register your models here.

admin.site.register(User)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Rent)
admin.site.register(Category)

