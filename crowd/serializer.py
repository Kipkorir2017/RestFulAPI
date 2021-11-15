from rest_framework import serializers
from .models import Initiative,Profile,Contributor,Wallet


class InitiativeSerializer(serializers.ModelSerializer):
               class Meta:
                              model = Initiative
                              fields="__all__"


class  ContributorSerializer(serializers.ModelSerializer):
               class Meta:
                              model=Contributor
                              fields="__all__"

class ProfileSerializer(serializers.ModelSerializer):
               class Meta:
                              model=Profile
                              fields="__all__"

class WalletSerializer(serializers.ModelSerializer):
               class Meta:
                              model=Wallet
                              fields="__all__"
