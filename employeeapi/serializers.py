# api will be able to communicate with mobile/web app.
# the api data is in python presentation. Before sending the data from the api, it has to be converted to json and vice versa

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
