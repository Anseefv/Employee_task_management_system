from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.



class EmployeesViewset(ModelViewSet):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeesSerialaizers
    queryset=Employees.objects.all()


class OprationViewset(ModelViewSet):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    serializer_class=OprationSerializers
    queryset=Operations.objects.all()

    def perform_create(self, serializer):
        pid=self.kwargs.get("pid")
        owner=Employees.objects.get(id=pid)
        return serializer.save(assigned_to=owner)





        
