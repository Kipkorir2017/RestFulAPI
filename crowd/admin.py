from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Initiative,Profile,Contributor,Wallet
# Register your models here.
admin.site.register(Initiative)
admin.site.register(Profile)
admin.site.register(Contributor)
admin.site.register(Wallet)