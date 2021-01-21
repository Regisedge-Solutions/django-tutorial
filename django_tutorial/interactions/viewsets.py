from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *


class InteractionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows InteractionType to be viewed or edited.
    """
    queryset = InteractionType.objects.all()
    serializer_class = InteractionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class InteractionSubTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows InteractionSubType to be viewed or edited.
    """
    queryset = InteractionSubType.objects.all()
    serializer_class = InteractionSubTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class DispositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Disposition to be viewed or edited.
    """
    queryset = Disposition.objects.all()
    serializer_class = DispositionSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubdispositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Subdisposition to be viewed or edited.
    """
    queryset = Subdisposition.objects.all()
    serializer_class = SubdispositionSerializer
    permission_classes = [permissions.IsAuthenticated]

class InteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Interaction to be viewed or edited.
    """
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated]

