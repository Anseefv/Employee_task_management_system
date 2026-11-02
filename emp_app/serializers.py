from rest_framework import serializers
from .models import*


class EmployeesSerialaizers(serializers.ModelSerializer):

    class Meta:

        model=Employees
        fields='__all__'
        read_only_fields=['id','joining_date']

class OprationSerializers(serializers.ModelSerializer):

    assigned_to=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Operations
        fields='__all__'
        read_only_fields=['id','assigned_to']

