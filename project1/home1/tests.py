from django.conf.urls import url
from django.contrib.auth.models import User
from django.http import response
from django.test import Client, TestCase
from django.urls import resolve, reverse
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Product
from .serializers import ProductSerializers, UserSerializers
# from .views import Auth, ProductDetail, ProductList, UserDetail, UserList
from .views import Auth, ProductListDetail, UserViewsets
# Create your tests here.

class TestUrls(APITestCase):
    def  test_login_urls(self):
        url =reverse('login')
        self.assertEquals(resolve(url).func.view_class, Auth)

    # def test_product_list_urls(self):
    #     url = reverse('product-list')
    #     self.assertEqual(resolve(url).func.view_class, ProductListDetail)

class TestModel(TestCase):
    def test_string_representation(self):
        product = Product(name="chau_acc")
        self.assertEqual(str(product), product.name)

class TestView(APITestCase):
    list_url = reverse("product-list")
    def setUp(self):
        self.user= User.objects.create_user(username='chau123', password='chau737701')
        Product.objects.create(id='1', name ='chau_aaa', status ='hello world', owner= self.user)
        Product.objects.create(id='2', name ='chau_bbb', status ='hello baby', owner= self.user)
        Product.objects.create(id='3', name ='chau_ccc', status ='hello girl', owner= self.user)
        Product.objects.create(id='4', name ='chau_ppp', status ='hello boy', owner= self.user)
        self.token= Token.objects.create(user= self.user)
        self.api_authentication()
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    def test_product_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["owner"], self.user.username)
        self.assertEqual(response.data["results"][1]["owner"], self.user.username)

    def test_product_list_filter_authenticated(self):

        response = self.client.get("/Proudct/" ,{"id":"2"} )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_create_authenticated(self):
        data = {'id':'5', 'name': 'chau_mmm', 'status':'hello'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["id"], data.id)

    def test_product_detail_authenticated(self):
        # serializer_data = ProductSerializers(instance=self.status).data
        response= self.client.get(reverse("product-detail", kwargs={"pk":4}))
        # print(reverse("product-detail", kwargs={"pk":10}))
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['user'], 'chau')
    
    def test_product_update_authenticated(self):
        data = {'id':'34', 'name': 'chau_ppp', 'status':'hello world'}
        response = self.client.put(reverse("product-detail", kwargs={"pk": 4}),data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detele_authenticated(self):
        response =self.client.delete(reverse("product-detail", kwargs={"pk":4}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


