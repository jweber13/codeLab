from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
	owner = serializers.Field(source='owner.username')
	class Meta:
		model = Employee
		fields = ('id', 'name', 'email', 'position', 'owner')

class UserSerializer(serializers.ModelSerializer):
	employee = serializers.PrimaryKeyRelatedField(many=True)
	class Meta:
		model = User
		fields = ('id', 'username', 'employee')
