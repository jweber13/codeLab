from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.authtoken.models import Token

class EmployeeTestCase(APITestCase):

	client = APIClient()
	factory = APIRequestFactory

	def setUp(self):
		# create super user with admin rights to use
		# employee request methods. test super user rights
		print 'test: SETUP'
		user = User.objects.create_superuser('tom', 'tom@vokalLabs.com', 'password')
		user.save()
		self.assertEqual('True', str(user.is_superuser))
	
	# create employees to be added
	emp_1 = {
	'name': 'john',
	'email': 'john@mailserver.com',
	'position': 'tmp'
	}
	
	emp_2 = {
	'name': 'lenny',
	'email': 'lenny@mail.com',
	'position': 'lead',
	}

	emp_3 = {
	'name': 'carl',
	'email': 'carl@gmail.com',
	'position': 'dev'
	}

	emp_4 = {
	'name': 'brenda',
	'email': 'brenda@accounts.net',
	'position': 'dev'
	}

	emp_5 = {
	'name': 'jenny',
	'email': 'jenny@something.com',
	'position': 'hr'
	}

	def test_index(self):
		# test that /employee/ exists and returns a 
		# status code of HTTP_200_OK
		print 'test: EXISTS'
		resp = self.client.get('/employee/')
		self.assertEqual(resp.status_code, 200)

	def test_login(self):
		# test login credentials. a super user has already been
		# created. Test failure and success
		print 'test: LOGIN'
		resp = self.client.login(username='lenny', password='secret')
		self.assertEqual('False', str(resp))
		resp = self.client.login(username='tom', password='password')
		self.assertEqual('True', str(resp))
		self.client.logout()

	def test_post_get(self):
		print 'test: POST/GET/DELETE'
		# test POST request without authentication
		resp = self.client.post('/employee/', self.emp_1, format='json')
		self.assertEqual(resp.status_code, 403)
		
		# test POST and GET requests
		self.client.login(username='tom', password='password')
		resp = self.client.post('/employee/', self.emp_1, format='json')
		self.assertEqual(resp.status_code, 201)
		resp = self.client.post('/employee/', self.emp_2, format='json')
		self.assertEqual(resp.status_code, 201)
		print str(resp.data)
		resp = self.client.get('/employee/')
		print 'GET: ' + str(resp.data)
		resp = self.client.get('/employee/1/')
		print 'GET: ' + str(resp.data)

		# test DELETE from /employee
		resp = self.client.delete('/employee/1/')
		self.assertEqual(resp.status_code, 204)
		resp = self.client.get('/employee/1/')
		print str(resp.data)
		
	def test_put(self):
		# test PUT request and verify successful status
		self.emp_2 = {
		'name': 'lenny',
		'email': 'lenny@gmail.com',
		'position': 'project lead'
		}
		self.client.login(username='tom', password='password')
		resp = self.client.put('/employee/2/', self.emp_2, format='json')
		self.assertEqual(resp.status_code, 201)
		print 'test: PUT' + str(resp.data)
