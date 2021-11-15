from django.shortcuts import render
from rest_framework import serializers
from rest_framework .response import Response
from .models import Initiative,Profile,Wallet,Contributor
from .serializer import  InitiativeSerializer,ProfileSerializer,ContributorSerializer,WalletSerializer
from rest_framework  import  viewsets

from crowd import serializer
# Create your views here.


class InitiativeList(viewsets.ModelViewSet):
               queryset=Initiative.objects.all()
               serializer_class=InitiativeSerializer

class ProfileList(viewsets.ModelViewSet):
               queryset=Profile.objects.all()
               serializer_class=ProfileSerializer

class ContributorList(viewsets.ModelViewSet):
               queryset=Contributor.objects.all()
               serializer_class=ContributorSerializer             

class WalletList(viewsets.ModelViewSet):
               queryset=Wallet.objects.all()
               serializer_class=WalletSerializer
