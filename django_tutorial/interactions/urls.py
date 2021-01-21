from django.urls import include, path
from rest_framework import routers
from django.urls import path

from . import views
from . import viewsets

router = routers.DefaultRouter()
router.register(r'interactiontypes', viewsets.InteractionTypeViewSet)
router.register(r'interactionsubtypes', viewsets.InteractionSubTypeViewSet)
router.register(r'dispositions', viewsets.DispositionViewSet)
router.register(r'subdispositions', viewsets.SubdispositionViewSet)
router.register(r'interactions', viewsets.InteractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
]



