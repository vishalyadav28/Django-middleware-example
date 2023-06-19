from .views import TestAPIViewset
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router=DefaultRouter()

router.register('TestAPIViewset',TestAPIViewset,basename='TestAPIViewset')
urlpatterns = [
    path('',include(router.urls)),
    
]