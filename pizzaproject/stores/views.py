from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer
from .model import Pizzeria

class PizzeriaListAPIView(generics.ListAPIView):
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaListSerializer	
