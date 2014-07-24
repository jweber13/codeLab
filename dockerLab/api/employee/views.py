from employee.models import Employee
from employee.serializers import EmployeeSerializer
from employee.serializers import UserSerializer
from employee.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

class EmployeeList(generics.ListCreateAPIView):
	def pre_save(self, obj):
		obj.owner = self.request.user
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
	def pre_save(self, obj):
		obj.owner = self.request.user
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
					IsOwnerOrReadOnly)
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
