from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, ' ',
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    receive_newsletter = models.BooleanField(default=False)
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email', ]




class Library(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=None, related_name='items', on_delete=models.CASCADE)
    library = models.ForeignKey(Library, null=True, related_name='library_books', on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=True, null=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    pages = models.IntegerField(blank=False, default=1, null=False)
    language = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title


class Rent(models.Model):
    book = models.ForeignKey(Book, related_name='rented_book', on_delete=models.CASCADE, unique=True)
    reader = models.ForeignKey(User, related_name='rented_by', on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    price = models.IntegerField(blank=False, default=0, null=False)

