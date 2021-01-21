from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

class CustomerTagsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CustomerTags to be viewed or edited.
    """
    queryset = CustomerTags.objects.all()
    serializer_class = CustomerTagsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

