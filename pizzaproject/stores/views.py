from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer, UserSerializer
from .models import Pizzeria
from django.contrib.auth import get_user_model

class PizzeriaListAPIView(generics.ListAPIView):
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaListSerializer	

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
	lookup_field = 'id'
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaCreateAPIView(generics.CreateAPIView):
	parser_classes = [MultiPartParser]
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	lookup_field = 'id'
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaDestroyAPIView(generics.DestroyAPIView):
	lookup_field = 'id'
	queryset = Pizzeria.objects.all()

class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer