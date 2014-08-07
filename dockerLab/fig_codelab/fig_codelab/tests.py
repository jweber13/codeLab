from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.authtoken.models import Token

class CodelabTestCase(APITestCase):
	client = APIClient()
	factory = APIRequestFactory

	def setUp(self):
		print 'test: SETUP'

	def testPrint(self):
		a = 'a'
		assertEqual(a, 'a')
