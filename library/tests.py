from django.test import TestCase
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import *
from .models import *

class UserTestCase(APITestCase):

    def setUp(self):
        self.data = {"username":"testinguser", "email":"testing@user.com",
                "first_name":"Firstname", "last_name":":LastName",
                "address":"USA", "about_me":"Something Something"}

    def test_users_view(self):

        response = self.client.get("http://127.0.0.1:8000/users/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_creation(self):

        response = self.client.post("http://127.0.0.1:8000/users/", self.data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


    def test_user_detailed_view(self):

        User.objects.create(username="testinguser", email="testing@user.com",
                first_name="Firstname", last_name="LastName",
                address="USA", about_me="Something Something")

        response = self.client.get("http://127.0.0.1:8000/users/1/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):

        User.objects.create(username="testinguser", email="testing@user.com",
                first_name="Firstname", last_name="LastName",
                address="USA", about_me="Something Something")

        response = self.client.delete("http://127.0.0.1:8000/users/1/")

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_update(self):


        User.objects.create(username="testinguser2", email="testing@user.com",
                first_name="Firstname", last_name="LastName",
                address="USA", about_me="Something Something")

        response = self.client.put("http://127.0.0.1:8000/users/1/", self.data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)


