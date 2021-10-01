from rest_framework import serializers
from .models import Company, Employee, Partnership

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('companies', 'name', 'location')

class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('user',)
 
class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'
 
class PartnershipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ('employee', 'company', 'post')
 