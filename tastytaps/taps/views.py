from rest_framework.permissions import IsAuthenticated

from .models import Beer
from .serializers import BeerSerializer

from rest_framework.viewsets import ModelViewSet


class BeersViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
