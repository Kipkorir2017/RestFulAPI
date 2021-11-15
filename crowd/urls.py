from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
router=routers.DefaultRouter()
router.register('wallet',views.WalletList )
router.register('initiative',views.InitiativeList )
router.register('contributor',views.ContributorList )
router.register('profile',views.ProfileList )





urlpatterns=[
              
             
               path('api/',include(router.urls)),

]

    
   