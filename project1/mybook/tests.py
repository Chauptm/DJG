from django.test import TestCase
from django.urls import reverse
from rest_framework import response, status
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from .models import Author, Book, Publisher

# Create your tests here.

class TestBook(APITestCase):
    url_list= reverse('publisher-list')

    def setUp(self) :
        # print(Publisher.objects.all())
        pub1= Publisher.objects.create(name='Van hoc')
        pub2= Publisher.objects.create(name='Tuoi tre')

    def test_list_book(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data.len(), 2)
        print(response.data)
        self.assertEqual(response.data[0]['id'], 1)

    # def test_create_book(self):
    #     data={'name':'Giai Phong'}
    #     response= self.client.post(self.url_list, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     # self.assertEqual
    #     print(response.data)
