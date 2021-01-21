from django.urls import include, path
from rest_framework import routers
from django.urls import path

from . import views
from . import viewsets

router = routers.DefaultRouter()
router.register(r'customertags', viewsets.CustomerTagsViewSet)
router.register(r'customers', viewsets.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
]