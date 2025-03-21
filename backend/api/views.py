from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView):
  serializer_class = NoteSerializer
  # must be auth'd and pass JWT
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Note.objects.filter(author=user)
  
  def perform_create(self, serializer):
    if serializer.is_valid():
      serializer.save(author=self.request.user)
    else:
      print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
      user = self.request.user
      return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
  # make sure user does not already exist
  queryset = User.objects.all()
  # necessary data (username, password)
  serializer_class = UserSerializer
  # allow unauthenticated users to use this view
  permission_classes = [AllowAny]
