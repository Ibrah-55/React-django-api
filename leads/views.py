from django.shortcuts import render
from .models import Lead
from rest_framework import generics
from .serializers import LeadSerializer

class LeadListCreate(generics.ListCreateAPIView):
    queryset= Lead.objects.all()
    serializer_class= LeadSerializer