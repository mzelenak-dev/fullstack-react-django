from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
  # make sure user does not already exist
  queryset = User.objects.all()
  # necessary data (username, password)
  serializer_class = UserSerializer
  # allow unauthenticated users to use this view
  permission_classes = [AllowAny]