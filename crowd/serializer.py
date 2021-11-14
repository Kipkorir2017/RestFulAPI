from rest_framework import serializers
from .models import Initiative,Profile,Contributor,Wallet


class InitiativeSerializer(serializers.ModelSerializer):
               class Meta:
                              model = Initiative
                              fields=('id', 'name','description','due_date','  target_amount ')


class  ContributorSerializer(serializers.ModelSerializer):
               class meta:
                              model=Contributor
                              fields=('id','initiative','contributor_name','phone_number','email')

class ProfileSerializer(serializers.ModelSerializer):
               class Meta:
                              model=Profile
                              fields=('id','initiative','contributor')

class WalletSerializer(serializers.ModelSerializer):
               class Meta:
                              model=Wallet
                              fields=('id','initiative','total_contributions')
